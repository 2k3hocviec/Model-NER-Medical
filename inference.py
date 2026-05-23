"""
inference.py
Dùng model đã train để:
1. Trích xuất triệu chứng từ câu người dùng (NER)
2. Gợi ý bác sĩ phù hợp (mapping)

Tích hợp vào chatbot chỉ cần gọi: predict(user_input)
"""

from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline # type: ignore
from symptom_mapping import (
    format_recommendation, 
    map_symptoms_to_doctors,
    get_doctors_for_specialty,
)

MODEL_PATH = "./output/medical-ner-model"


def load_ner_pipeline(model_path: str = MODEL_PATH):
    """Load model NER đã train"""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)

    ner_pipeline = pipeline(
        "ner",
        model=model,
        tokenizer=tokenizer,
        aggregation_strategy="simple",  # Gộp B- và I- thành 1 entity
    )
    return ner_pipeline


def extract_symptoms(text: str, ner_pipeline) -> list[str]:
    """
    Trích xuất triệu chứng từ văn bản đầu vào
    """
    entities = ner_pipeline(text)
    symptoms = []
    for ent in entities:
        if ent["entity_group"] == "SYMPTOM" and ent["score"] > 0.3:
            symptoms.append(ent["word"].strip())
    return symptoms


def predict(user_input: str, ner_pipeline) -> dict:
    """
    Hàm chính để tích hợp vào chatbot
    
    Input:  chuỗi văn bản từ người dùng
    Output: dict gồm symptoms, doctors và recommendations
    """
    symptoms = extract_symptoms(user_input, ner_pipeline)
    
    if not symptoms:
        return {
            "symptoms": [],
            "doctors": {},
            "message": (
                "Xin lỗi, tôi chưa nhận ra triệu chứng cụ thể trong câu bạn mô tả. "
                "Bạn thử mô tả rõ hơn nhé? Ví dụ: đau đầu, sốt, ho, đau bụng..."
            )
        }

    # Lấy mapping chuyên khoa từ triệu chứng
    specialties = map_symptoms_to_doctors(symptoms)
    
    # Tạo dict bác sĩ cụ thể theo chuyên khoa
    doctors_with_specialists = {}
    for specialty in specialties.keys():
        doctors_with_specialists[specialty] = get_doctors_for_specialty(specialty)
    
    # Tạo thông điệp tư vấn chi tiết
    recommendation_text = format_recommendation(symptoms)

    return {
        "symptoms": symptoms,
        "specialties": specialties,
        "doctors": doctors_with_specialists,
        "message": recommendation_text,
    }


# ── Test chạy thử ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Loading model...")
    ner = load_ner_pipeline()

    test_cases = [
        "Tôi bị đau đầu dữ dội và sốt cao từ hôm qua",
        "Mấy ngày nay tôi bị sổ mũi, hắt hơi và đau họng",
        "Tim tôi đập nhanh, khó thở và tức ngực",
        "Tôi bị đau bụng quặn và tiêu chảy liên tục",
    ]

    print("Nhập 'exit' hoặc 'quit' để dừng chương trình.\n")

    while True:
        # Lấy dữ liệu nhập vào từ bàn phím
        text = input("Nhập văn bản của bạn: ").strip()
        
        # Kiểm tra điều kiện để thoát vòng lặp
        if text.lower() in ['exit', 'quit', '']:
            print("Đã thoát chương trình.")
            break
            
        print(f"\n{'='*60}")
        print(f"Input : {text}")
        
        # Dự đoán và in kết quả
        result = predict(text, ner)
        print(f"Trieu chung: {result['symptoms']}")
        print()
        print(result["message"])
        print(f"={''*60}\n")