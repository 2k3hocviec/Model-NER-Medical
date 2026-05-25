"""Shared specialty labels for the specialty-aware NER model."""

from __future__ import annotations

from typing import Any


SPECIALTY_CATALOG = {
    "GENERAL_MEDICINE": {"name": "Nội khoa", "slug": "noi-khoa"},
    "CARDIOLOGY": {"name": "Tim mạch", "slug": "tim-mach"},
    "RESPIRATORY": {"name": "Hô hấp", "slug": "ho-hap"},
    "PEDIATRICS": {"name": "Nhi khoa", "slug": "nhi-khoa"},
    "DERMATOLOGY": {"name": "Da liễu", "slug": "da-lieu"},
    "NEUROLOGY": {"name": "Thần kinh", "slug": "than-kinh"},
    "ENT": {"name": "Tai mũi họng", "slug": "tai-mui-hong"},
    "OB_GYN": {"name": "Sản phụ khoa", "slug": "san-phu-khoa"},
    "ORTHOPEDICS": {"name": "Cơ xương khớp", "slug": "co-xuong-khop"},
    "OPHTHALMOLOGY": {"name": "Mắt", "slug": "mat"},
    "GASTROENTEROLOGY": {"name": "Tiêu hóa", "slug": "tieu-hoa"},
    "DENTISTRY": {"name": "Răng hàm mặt", "slug": "rang-ham-mat"},
    "UROLOGY": {"name": "Tiết niệu", "slug": "tiet-nieu"},
    "ENDOCRINOLOGY": {"name": "Nội tiết", "slug": "noi-tiet"},
    "PSYCHIATRY": {"name": "Tâm thần", "slug": "tam-than"},
    "ONCOLOGY": {"name": "Ung bướu", "slug": "ung-buou"},
    "EMERGENCY": {"name": "Cấp cứu", "slug": "cap-cuu"},
}

# Order matters for composite legacy values. Critical/specific specialties win.
LEGACY_SPECIALTY_HINTS = [
    ("Cấp cứu", "EMERGENCY"),
    ("Ung bướu", "ONCOLOGY"),
    ("Sản phụ khoa", "OB_GYN"),
    ("Nhi khoa", "PEDIATRICS"),
    ("Tâm thần", "PSYCHIATRY"),
    ("Tim mạch", "CARDIOLOGY"),
    ("Hô hấp", "RESPIRATORY"),
    ("Thần kinh", "NEUROLOGY"),
    ("Nội tiết", "ENDOCRINOLOGY"),
    ("Tiết niệu", "UROLOGY"),
    ("Cơ xương khớp", "ORTHOPEDICS"),
    ("Da liễu", "DERMATOLOGY"),
    ("Nhãn khoa", "OPHTHALMOLOGY"),
    ("Răng", "DENTISTRY"),
    ("Tai Mũi Họng", "ENT"),
    ("Tiêu hóa", "GASTROENTEROLOGY"),
    ("Nội khoa", "GENERAL_MEDICINE"),
    ("Đa khoa", "GENERAL_MEDICINE"),
]


def build_label_maps() -> tuple[dict[str, int], dict[int, str]]:
    labels = ["O"]
    for code in SPECIALTY_CATALOG:
        labels.extend([f"B-{code}", f"I-{code}"])
    label2id = {label: index for index, label in enumerate(labels)}
    return label2id, {index: label for label, index in label2id.items()}


LABEL2ID, ID2LABEL = build_label_maps()


def validate_specialty_code(code: str) -> str:
    if code not in SPECIALTY_CATALOG:
        valid = ", ".join(SPECIALTY_CATALOG)
        raise ValueError(f"Unknown specialty label '{code}'. Use one of: {valid}")
    return code


def code_from_legacy_specialty(specialty: str) -> str | None:
    for keyword, code in LEGACY_SPECIALTY_HINTS:
        if keyword.casefold() in specialty.casefold():
            return code
    return None

def specialty_payload(code: str) -> dict[str, Any]:
    validate_specialty_code(code)
    return {"code": code, **SPECIALTY_CATALOG[code]}
