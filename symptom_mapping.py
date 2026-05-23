"""
symptom_mapping.py
Ánh xạ triệu chứng → chuyên khoa bác sĩ phù hợp
"""

SYMPTOM_DOCTOR_MAP = {
    # Nội khoa / Đa khoa
    "sốt": "Bác sĩ Đa khoa / Nội khoa",
    "sốt cao": "Bác sĩ Đa khoa / Nội khoa",
    "mệt mỏi": "Bác sĩ Đa khoa / Nội khoa",
    "ớn lạnh": "Bác sĩ Đa khoa / Nội khoa",
    "sụt cân": "Bác sĩ Nội khoa / Nội tiết",
    "khát nước": "Bác sĩ Nội tiết (nghi tiểu đường)",
    "đổ mồ hôi đêm": "Bác sĩ Nội khoa / Lao phổi",

    # Tai Mũi Họng
    "sổ mũi": "Bác sĩ Tai Mũi Họng",
    "hắt hơi": "Bác sĩ Tai Mũi Họng",
    "đau họng": "Bác sĩ Tai Mũi Họng",
    "ù tai": "Bác sĩ Tai Mũi Họng",
    "nghe kém": "Bác sĩ Tai Mũi Họng",
    "đau trong tai": "Bác sĩ Tai Mũi Họng",
    "nghẹt mũi": "Bác sĩ Tai Mũi Họng",
    "chảy mũi": "Bác sĩ Tai Mũi Họng",

    # Hô hấp / Phổi
    "ho": "Bác sĩ Hô hấp",
    "khó thở": "Bác sĩ Hô hấp / Tim mạch",
    "ho khan": "Bác sĩ Hô hấp",
    "tức ngực": "Bác sĩ Tim mạch / Hô hấp",
    "ho ra máu": "Bác sĩ Hô hấp / Lao phổi",
    "thở khò khè": "Bác sĩ Hô hấp (nghi hen suyễn)",

    # Tim mạch
    "đau ngực": "Bác sĩ Tim mạch",
    "tim đập nhanh": "Bác sĩ Tim mạch",
    "hồi hộp": "Bác sĩ Tim mạch",
    "ngất xỉu": "Bác sĩ Tim mạch / Thần kinh",

    # Thần kinh / Tâm thần
    "đau đầu": "Bác sĩ Thần kinh",
    "đau nửa đầu": "Bác sĩ Thần kinh (chuyên đau đầu)",
    "chóng mặt": "Bác sĩ Thần kinh / Tai Mũi Họng",
    "mất thăng bằng": "Bác sĩ Thần kinh",
    "tê bì chân tay": "Bác sĩ Thần kinh / Cơ xương khớp",
    "mất ngủ": "Bác sĩ Tâm thần / Thần kinh",
    "lo âu": "Bác sĩ Tâm thần",
    "cáu gắt": "Bác sĩ Tâm thần",
    "trầm cảm": "Bác sĩ Tâm thần",
    "run tay": "Bác sĩ Thần kinh",
    "run chân": "Bác sĩ Thần kinh",
    "run rẩy": "Bác sĩ Thần kinh",
    "tay run": "Bác sĩ Thần kinh",

    # Tiêu hóa
    "đau dạ dày": "Bác sĩ Tiêu hóa / Nội khoa",
    "đau bụng": "Bác sĩ Tiêu hóa / Nội khoa",
    "đau quặn bụng": "Bác sĩ Tiêu hóa",
    "buồn nôn": "Bác sĩ Tiêu hóa / Nội khoa",
    "tiêu chảy": "Bác sĩ Tiêu hóa / Nội khoa",
    "táo bón": "Bác sĩ Tiêu hóa",
    "đầy hơi": "Bác sĩ Tiêu hóa",
    "chướng bụng": "Bác sĩ Tiêu hóa",
    "ợ chua": "Bác sĩ Tiêu hóa (nghi trào ngược)",
    "mất nước": "Bác sĩ Cấp cứu / Tiêu hóa",
    "chảy máu": "Bác sĩ Tiêu hóa",
    "trĩ": "Bác sĩ Tiêu hóa",
    "sa búi trĩ": "Bác sĩ Tiêu hóa",
    "đau hậu môn": "Bác sĩ Tiêu hóa",
    "chảy máu hậu môn": "Bác sĩ Tiêu hóa",
    "đi ngoài ra máu": "Bác sĩ Tiêu hóa",
    "rát hậu môn": "Bác sĩ Tiêu hóa",

    # Cơ xương khớp
    "đau lưng dưới": "Bác sĩ Cơ xương khớp / Phục hồi chức năng",
    "đau lưng": "Bác sĩ Cơ xương khớp",
    "mỏi cơ": "Bác sĩ Cơ xương khớp / Phục hồi chức năng",
    "sưng đau": "Bác sĩ Cơ xương khớp",
    "cứng khớp": "Bác sĩ Cơ xương khớp (nghi viêm khớp)",
    "đau khớp": "Bác sĩ Cơ xương khớp",

    # Da liễu
    "nổi mẩn đỏ": "Bác sĩ Da liễu",
    "ngứa ngáy": "Bác sĩ Da liễu / Dị ứng",
    "da khô": "Bác sĩ Da liễu / Nội tiết",
    "rụng tóc": "Bác sĩ Da liễu / Nội tiết",
    "mụn": "Bác sĩ Da liễu",
    "vàng da": "Bác sĩ Da liễu",

    # Nhãn khoa
    "nhìn mờ": "Bác sĩ Nhãn khoa",
    "mắt đỏ": "Bác sĩ Nhãn khoa",
    "chảy nước mắt": "Bác sĩ Nhãn khoa",
    "đau mắt": "Bác sĩ Nhãn khoa",

    # Răng hàm mặt
    "đau răng": "Bác sĩ Răng hàm mặt",
    "sưng nướu": "Bác sĩ Răng hàm mặt",
    "chảy máu nướu": "Bác sĩ Răng hàm mặt",

    # Tiết niệu / Thận
    "đi tiểu nhiều lần": "Bác sĩ Tiết niệu / Nội tiết",
    "tiểu buốt": "Bác sĩ Tiết niệu",
    "máu trong nước tiểu": "Bác sĩ Tiết niệu / Thận",
    "đau thận": "Bác sĩ Thận / Tiết niệu",

    # Nội tiết
    "tăng cân": "Bác sĩ Nội tiết / Dinh dưỡng",
    "rụng nhiều": "Bác sĩ Nội tiết / Da liễu",
}

SPECIALTY_INFO = {
    "Bác sĩ Đa khoa / Nội khoa": {
        "icon": "🏥",
        "description": "Khám tổng quát, chẩn đoán ban đầu và điều trị bệnh thông thường"
    },
    "Bác sĩ Tai Mũi Họng": {
        "icon": "👂",
        "description": "Chuyên điều trị các bệnh về tai, mũi, họng, thanh quản"
    },
    "Bác sĩ Tim mạch": {
        "icon": "❤️",
        "description": "Chuyên về tim mạch, huyết áp, mạch máu"
    },
    "Bác sĩ Hô hấp": {
        "icon": "🫁",
        "description": "Chuyên về phổi, hen suyễn, viêm phế quản, COPD"
    },
    "Bác sĩ Tiêu hóa": {
        "icon": "🦠",
        "description": "Chuyên về dạ dày, ruột, gan, tụy và đường tiêu hóa"
    },
    "Bác sĩ Thần kinh": {
        "icon": "🧠",
        "description": "Chuyên về não bộ, hệ thần kinh, đau đầu, đột quỵ"
    },
    "Bác sĩ Cơ xương khớp": {
        "icon": "🦴",
        "description": "Chuyên về xương khớp, cột sống, cơ và mô liên kết"
    },
    "Bác sĩ Da liễu": {
        "icon": "🩹",
        "description": "Chuyên về da, tóc, móng và các bệnh dị ứng da"
    },
    "Bác sĩ Nhãn khoa": {
        "icon": "👁️",
        "description": "Chuyên về mắt và thị lực"
    },
    "Bác sĩ Răng hàm mặt": {
        "icon": "🦷",
        "description": "Chuyên về răng, nướu, xương hàm và miệng"
    },
    "Bác sĩ Tiết niệu": {
        "icon": "🧪",
        "description": "Chuyên về thận, bàng quang, đường tiết niệu"
    },
    "Bác sĩ Tâm thần": {
        "icon": "🧘",
        "description": "Chuyên về sức khỏe tâm thần, lo âu, trầm cảm, rối loạn tâm thần"
    },
    "Bác sĩ Nội tiết": {
        "icon": "⚗️",
        "description": "Chuyên về hormone, tuyến giáp, tiểu đường, tuyến thượng thận"
    },
}


# Danh sách bác sĩ cụ thể theo chuyên khoa
DOCTORS_BY_SPECIALTY = {
    "Bác sĩ Đa khoa / Nội khoa": [
        {"name": "BS. Nguyễn Văn A", "experience": "15 năm", "phone": "0912345678", "rating": 4.8},
        {"name": "BS. Trần Thị B", "experience": "12 năm", "phone": "0987654321", "rating": 4.7},
        {"name": "BS. Phạm Văn C", "experience": "10 năm", "phone": "0901234567", "rating": 4.6},
    ],
    "Bác sĩ Tai Mũi Họng": [
        {"name": "BS. Vũ Đức D", "experience": "18 năm", "phone": "0913456789", "rating": 4.9},
        {"name": "BS. Lê Thị E", "experience": "14 năm", "phone": "0988765432", "rating": 4.8},
    ],
    "Bác sĩ Tim mạch": [
        {"name": "BS. Hoàng Văn F", "experience": "20 năm", "phone": "0914567890", "rating": 4.9},
        {"name": "BS. Đỗ Thị G", "experience": "16 năm", "phone": "0989876543", "rating": 4.8},
        {"name": "BS. Đặng Văn H", "experience": "13 năm", "phone": "0902345678", "rating": 4.7},
    ],
    "Bác sĩ Hô hấp": [
        {"name": "BS. Bùi Văn I", "experience": "17 năm", "phone": "0915678901", "rating": 4.8},
        {"name": "BS. Cao Thị J", "experience": "11 năm", "phone": "0990987654", "rating": 4.7},
    ],
    "Bác sĩ Tiêu hóa": [
        {"name": "BS. Tạ Văn K", "experience": "19 năm", "phone": "0916789012", "rating": 4.9},
        {"name": "BS. Vương Thị L", "experience": "15 năm", "phone": "0991234567", "rating": 4.8},
        {"name": "BS. Lý Văn M", "experience": "12 năm", "phone": "0903456789", "rating": 4.7},
    ],
    "Bác sĩ Thần kinh": [
        {"name": "BS. Nông Văn N", "experience": "21 năm", "phone": "0917890123", "rating": 4.9},
        {"name": "BS. Sơn Thị O", "experience": "18 năm", "phone": "0992345678", "rating": 4.9},
        {"name": "BS. Trịnh Văn P", "experience": "14 năm", "phone": "0904567890", "rating": 4.8},
    ],
    "Bác sĩ Cơ xương khớp": [
        {"name": "BS. Hồ Văn Q", "experience": "16 năm", "phone": "0918901234", "rating": 4.8},
        {"name": "BS. Từ Thị R", "experience": "13 năm", "phone": "0993456789", "rating": 4.7},
    ],
    "Bác sĩ Da liễu": [
        {"name": "BS. Lâm Văn S", "experience": "14 năm", "phone": "0919012345", "rating": 4.7},
        {"name": "BS. Chu Thị T", "experience": "11 năm", "phone": "0994567890", "rating": 4.6},
    ],
    "Bác sĩ Nhãn khoa": [
        {"name": "BS. Dương Văn U", "experience": "17 năm", "phone": "0920123456", "rating": 4.8},
        {"name": "BS. Lê Thị V", "experience": "15 năm", "phone": "0995678901", "rating": 4.8},
    ],
    "Bác sĩ Răng hàm mặt": [
        {"name": "BS. Quách Văn W", "experience": "12 năm", "phone": "0921234567", "rating": 4.7},
    ],
    "Bác sĩ Tiết niệu": [
        {"name": "BS. Trương Văn X", "experience": "18 năm", "phone": "0922345678", "rating": 4.8},
        {"name": "BS. Hương Thị Y", "experience": "15 năm", "phone": "0996789012", "rating": 4.8},
    ],
    "Bác sĩ Tâm thần": [
        {"name": "BS. Võ Văn Z", "experience": "19 năm", "phone": "0923456789", "rating": 4.9},
        {"name": "BS. Kim Thị AA", "experience": "16 năm", "phone": "0997890123", "rating": 4.8},
    ],
    "Bác sĩ Nội tiết": [
        {"name": "BS. Dư Văn AB", "experience": "15 năm", "phone": "0924567890", "rating": 4.7},
        {"name": "BS. Giang Thị AC", "experience": "13 năm", "phone": "0998901234", "rating": 4.7},
    ],
}


def get_doctors_for_specialty(specialty: str) -> list:
    """
    Lấy danh sách bác sĩ theo chuyên khoa
    
    Args:
        specialty: Tên chuyên khoa
    
    Returns:
        Danh sách bác sĩ hoặc list rỗng nếu chuyên khoa không tồn tại
    """
    return DOCTORS_BY_SPECIALTY.get(specialty, [])


def map_symptoms_to_doctors(symptoms: list[str]) -> dict:
    """
    Input:  danh sách triệu chứng đã được NER model trích xuất
    Output: dict gồm {specialty: [symptoms]}
    """
    result = {}

    for symptom in symptoms:
        symptom_lower = symptom.lower().strip()
        doctor = None

        # Exact match
        if symptom_lower in SYMPTOM_DOCTOR_MAP:
            doctor = SYMPTOM_DOCTOR_MAP[symptom_lower]
        else:
            # Fuzzy: kiểm tra từ khóa con
            for key, val in SYMPTOM_DOCTOR_MAP.items():
                if key in symptom_lower or symptom_lower in key:
                    doctor = val
                    break

        if doctor:
            if doctor not in result:
                result[doctor] = []
            result[doctor].append(symptom)

    return result


def format_recommendation(symptoms: list[str]) -> str:
    """Trả về chuỗi tư vấn người dùng kèm bác sĩ cụ thể"""
    mapping = map_symptoms_to_doctors(symptoms)

    if not mapping:
        return (
            "Xin lỗi, tôi chưa nhận ra triệu chứng bạn mô tả.\n"
            "Bạn có thể mô tả chi tiết hơn không? Ví dụ: đau đầu, sốt, ho, đau bụng..."
        )

    lines = ["Dựa trên các triệu chứng của bạn, tôi gợi ý:\n"]

    for specialty, syms in mapping.items():
        info = SPECIALTY_INFO.get(specialty, {})
        icon = info.get("icon", "🏥")
        desc = info.get("description", "")
        
        # Hiển thị chuyên khoa
        lines.append(f"{icon} **{specialty}**")
        lines.append(f"   Triệu chứng liên quan: {', '.join(syms)}")
        lines.append(f"   {desc}\n")
        
        # Hiển thị bác sĩ cụ thể
        doctors = get_doctors_for_specialty(specialty)
        if doctors:
            lines.append("   📋 Bác sĩ khuyên cáo:")
            for i, doc in enumerate(doctors, 1):
                rating_stars = "⭐" * int(doc["rating"])
                lines.append(
                    f"      {i}. {doc['name']} ({doc['experience']} kinh nghiệm) "
                    f"- {rating_stars} ({doc['rating']}/5)"
                )
                lines.append(f"         📞 {doc['phone']}")
            lines.append("")

    lines.append("⚠️ Lưu ý: Đây chỉ là tư vấn ban đầu. Vui lòng đến cơ sở y tế để được khám chính xác.")
    return "\n".join(lines)


# --- Test thử ---
if __name__ == "__main__":
    test_symptoms = ["đau đầu", "sổ mũi", "sốt cao", "mệt mỏi"]
    print(format_recommendation(test_symptoms))
