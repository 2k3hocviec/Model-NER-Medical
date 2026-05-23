"""
model_api.py
FastAPI server để chạy model NER
"""

from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from pydantic import BaseModel # type: ignore
import os
from transformers import pipeline  # type: ignore
from symptom_mapping import map_symptoms_to_doctors, get_doctors_for_specialty, SPECIALTY_INFO

# ─ Cấu hình ─────────────────────────────────────────────────────────
MODEL_PATH = "./output/medical-ner-model"
PORT = 5555

app = FastAPI(title="Medical NER Model API")

# CORS - cho phép NestJS gọi từ localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model vào memory
ner_pipeline = None


class DoctorInfo(BaseModel):
    """Thông tin bác sĩ"""
    name: str
    experience: str
    phone: str
    rating: float


class DoctorRecommendation(BaseModel):
    """Khuyến cáo bác sĩ theo chuyên khoa"""
    specialty: str
    icon: str
    description: str
    symptoms_matched: list[str]
    doctors: list[DoctorInfo]


class SymptomRequest(BaseModel):
    """Request body"""
    text: str


class SymptomResponse(BaseModel):
    """Response body"""
    symptoms: list[str]
    confidence_scores: list[float]
    message: str
    doctors: list[DoctorRecommendation]


@app.on_event("startup")
async def load_model():
    """Load model khi server khởi động"""
    global ner_pipeline
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model không tìm thấy: {MODEL_PATH}")
        return
    
    try:
        print(f"📦 Loading model từ {MODEL_PATH}...")
        ner_pipeline = pipeline(
            "ner",
            model=MODEL_PATH,
            tokenizer=MODEL_PATH,
            aggregation_strategy="simple",
        )
        print("✓ Model loaded thành công!")
    except Exception as e:
        print(f"❌ Lỗi load model: {e}")


@app.get("/health")
async def health_check():
    """Kiểm tra health"""
    return {
        "status": "ok",
        "model_loaded": ner_pipeline is not None,
    }


@app.post("/api/extract-symptoms", response_model=SymptomResponse)
async def extract_symptoms(request: SymptomRequest):
    """
    Trích xuất triệu chứng từ văn bản + gợi ý bác sĩ
    
    Example:
        POST /api/extract-symptoms
        {
            "text": "Tôi bị ho có đờm và sốt cao"
        }
    """
    if not ner_pipeline:
        raise HTTPException(status_code=500, detail="Model chưa load")
    
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text không được trống")
    
    try:
        # Gọi model
        entities = ner_pipeline(request.text)
        
        symptoms = []
        scores = []
        
        for ent in entities:
            if ent["entity_group"] == "SYMPTOM":
                symptoms.append(ent["word"].strip())
                scores.append(float(ent["score"]))
        
        # Map symptoms to doctors/specialties
        specialties_map = map_symptoms_to_doctors(symptoms)
        
        # Build doctor recommendations
        doctors_recommendations = []
        for specialty, symptoms_list in specialties_map.items():
            spec_info = SPECIALTY_INFO.get(specialty, {})
            doctors_list = get_doctors_for_specialty(specialty)
            
            # Convert doctors dict to DoctorInfo objects
            doctor_infos = [
                DoctorInfo(
                    name=doc["name"],
                    experience=doc["experience"],
                    phone=doc["phone"],
                    rating=doc["rating"]
                )
                for doc in doctors_list
            ]
            
            doctors_recommendations.append(
                DoctorRecommendation(
                    specialty=specialty,
                    icon=spec_info.get("icon", "🏥"),
                    description=spec_info.get("description", ""),
                    symptoms_matched=symptoms_list,
                    doctors=doctor_infos
                )
            )
        
        message = (
            f"Tìm thấy {len(symptoms)} triệu chứng"
            if symptoms
            else "Không tìm thấy triệu chứng nào"
        )
        
        return SymptomResponse(
            symptoms=symptoms,
            confidence_scores=scores,
            message=message,
            doctors=doctors_recommendations,
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn # type: ignore
    print("\n" + "="*70)
    print("🚀 Medical NER Model API")
    print("="*70)
    print(f"Server chạy tại: http://localhost:{PORT}")
    print(f"Health check: http://localhost:{PORT}/health")
    print(f"API docs: http://localhost:{PORT}/docs")
    print("="*70 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=PORT) 
