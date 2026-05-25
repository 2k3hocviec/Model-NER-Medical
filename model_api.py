"""FastAPI service for extracting symptoms and their specialty labels."""

import os

from fastapi import FastAPI, HTTPException  # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore
from pydantic import BaseModel  # type: ignore
from transformers import pipeline  # type: ignore

from inference import extract_specialty_symptoms


MODEL_PATH = "./output/medical-ner-model"
PORT = 5555

app = FastAPI(title="Medical Specialty NER API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ner_pipeline = None


class SymptomRequest(BaseModel):
    text: str


class DetectedSymptom(BaseModel):
    name: str
    confidence: float
    specialty_code: str
    specialty_name: str
    specialty_slug: str


class SpecialtyRecommendation(BaseModel):
    code: str
    name: str
    slug: str
    symptoms_matched: list[str]


class SymptomResponse(BaseModel):
    symptoms: list[DetectedSymptom]
    specialties: list[SpecialtyRecommendation]
    message: str


@app.on_event("startup")
async def load_model():
    """Load the NER model once when the AI service starts."""
    global ner_pipeline
    if not os.path.exists(MODEL_PATH):
        print(f"Model khong tim thay: {MODEL_PATH}")
        return
    try:
        ner_pipeline = pipeline(
            "ner",
            model=MODEL_PATH,
            tokenizer=MODEL_PATH,
            aggregation_strategy="simple",
        )
        print(f"Model da load: {MODEL_PATH}")
    except Exception as error:
        print(f"Loi load model: {error}")


@app.get("/health")
async def health_check():
    return {"status": "ok", "model_loaded": ner_pipeline is not None}


@app.post("/api/extract-symptoms", response_model=SymptomResponse)
async def extract_symptoms(request: SymptomRequest):
    if not ner_pipeline:
        raise HTTPException(status_code=503, detail="Model chua load")
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text khong duoc trong")

    detected = extract_specialty_symptoms(request.text, ner_pipeline)
    symptoms = [
        DetectedSymptom(
            name=item["name"],
            confidence=item["confidence"],
            specialty_code=item["specialty"]["code"],
            specialty_name=item["specialty"]["name"],
            specialty_slug=item["specialty"]["slug"],
        )
        for item in detected
    ]

    grouped: dict[str, SpecialtyRecommendation] = {}
    for symptom in symptoms:
        if symptom.specialty_code not in grouped:
            grouped[symptom.specialty_code] = SpecialtyRecommendation(
                code=symptom.specialty_code,
                name=symptom.specialty_name,
                slug=symptom.specialty_slug,
                symptoms_matched=[],
            )
        grouped[symptom.specialty_code].symptoms_matched.append(symptom.name)

    message = (
        f"Tìm thấy {len(symptoms)} triệu chứng và {len(grouped)} chuyên khoa phù hợp."
        if symptoms
        else "Không tìm thấy triệu chứng có độ tin cậy đủ cao."
    )
    return SymptomResponse(
        symptoms=symptoms,
        specialties=list(grouped.values()),
        message=message,
    )


if __name__ == "__main__":
    import uvicorn  # type: ignore

    uvicorn.run(app, host="0.0.0.0", port=PORT)
