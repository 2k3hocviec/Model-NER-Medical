# 🏥 Medical NER Chatbot — Hướng dẫn sử dụng

Hệ thống tư vấn y tế tự động gồm 2 bước:
1. **NER** — Trích xuất triệu chứng từ câu người dùng
2. **Mapping** — Ánh xạ triệu chứng → chuyên khoa bác sĩ phù hợp

---

## 📁 Cấu trúc thư mục

```
medical_ner/
├── data/
│   ├── dataset.json          ← Dataset gốc tiếng Việt
│   ├── dataset_specialty.json ← Nhãn NER theo chuyên khoa để train
│   ├── train_processed.json  ← Sau khi chạy prepare_data.py
│   └── val_processed.json
├── output/
│   └── medical-ner-model/    ← Model sau khi train xong
├── symptom_mapping.py        ← Logic ánh xạ triệu chứng → bác sĩ
├── prepare_data.py           ← Tiền xử lý data
├── train.py                  ← Training script
├── inference.py              ← Dùng model để predict
└── README.md
```

---

## ⚙️ Cài đặt

```bash
pip install transformers torch datasets seqeval
# Nếu dùng PhoBERT (khuyên dùng cho tiếng Việt):
pip install transformers[sentencepiece]
```

---

## 🚀 Chạy theo thứ tự

### Bước 0 — Tạo nhãn chuyên khoa cho NER

Model mới học trực tiếp entity theo chuyên khoa, ví dụ `CARDIOLOGY`,
`RESPIRATORY`, `NEUROLOGY`, thay vì nhãn chung `SYMPTOM`.

```bash
python label_dataset_specialties.py
```

Script tạo `data/dataset_specialty.json`, tự sửa các offset tìm được và suy ra
nhãn ban đầu từ mapping cũ. Trước khi train, tìm và sửa mọi nhãn
`REVIEW_REQUIRED` trong file này; `suggested_label`, nếu có, là khoa gợi ý
cho entity đang sai offset. Một entity phải có đúng một chuyên khoa chính;
các cảnh báo cấp cứu vẫn nên xử lý bằng rule riêng.

### Bước 1 — Chuẩn bị data
```bash
python prepare_data.py
```
> Chuyển `data/dataset_specialty.json` → `train_processed.json` + `val_processed.json`

### Bước 2 — Train model
```bash
python train.py
```
> Model lưu vào `output/medical-ner-model/`  
> Với 20 mẫu: train nhanh (~2–5 phút CPU). Nên bổ sung thêm data để model tốt hơn.

### Bước 3 — Test inference
```bash
python inference.py
```

---

## 🔌 Tích hợp vào Chatbot

```python
from inference import load_ner_pipeline, predict

# Khởi tạo 1 lần khi server start
ner_pipeline = load_ner_pipeline()

# Gọi mỗi khi nhận tin nhắn từ user
def handle_user_message(user_text: str) -> str:
    result = predict(user_text, ner_pipeline)
    return result["message"]

# Ví dụ:
response = handle_user_message("Tôi bị đau đầu và sốt cao")
print(response)
```

### Response API cho backend đặt lịch

`POST /api/extract-symptoms` trả về triệu chứng kèm slug chuyên khoa để
backend tra bảng `Specialty` và danh sách bác sĩ thật:

```json
{
  "symptoms": [
    {
      "name": "đau ngực",
      "confidence": 0.91,
      "specialty_code": "CARDIOLOGY",
      "specialty_name": "Tim mạch",
      "specialty_slug": "tim-mach"
    }
  ],
  "specialties": [
    {
      "code": "CARDIOLOGY",
      "name": "Tim mạch",
      "slug": "tim-mach",
      "symptoms_matched": ["đau ngực"]
    }
  ],
  "message": "Tìm thấy 1 triệu chứng và 1 chuyên khoa phù hợp."
}
```

Các slug AI có thể dự đoán nhưng backend hiện chưa seed như `noi-khoa`,
`ho-hap`, `noi-tiet`, `tam-than`, `ung-buou`, `cap-cuu`, `tiet-nieu` và
`rang-ham-mat` cần được thêm vào bảng `Specialty` trước khi đưa vào luồng đặt
lịch.

---

## 📊 Mở rộng dataset

Dataset hiện tại vẫn ở quy mô demo; nên bổ sung thêm mẫu sau khi đã làm sạch
offset và nhãn chuyên khoa. Khuyến nghị tối thiểu **200–500 mẫu** để đánh giá
một prototype có ý nghĩa hơn.

### Cách thêm data vào `data/dataset.json`:

```json
{
  "text": "Tôi bị đau bụng và sốt nhẹ",
  "entities": [
    {"start": 7, "end": 15, "label": "GASTROENTEROLOGY", "text": "đau bụng"},
    {"start": 19, "end": 26, "label": "GENERAL_MEDICINE", "text": "sốt nhẹ"}
  ]
}
```

> **Lưu ý `start`/`end`**: đây là chỉ số ký tự trong chuỗi `text`.  
> Dùng Python để kiểm tra: `text[start:end]` phải bằng đúng triệu chứng.

---

## 🤖 Model được dùng

| Model | Ngôn ngữ | Ghi chú |
|-------|----------|---------|
| `vinai/phobert-base` | Tiếng Việt | **Khuyên dùng** — được train trên corpus VN |
| `bert-base-multilingual-cased` | Đa ngôn ngữ | Dự phòng nếu không cài được PhoBERT |

---

## ⚠️ Lưu ý quan trọng

- Hệ thống này **chỉ mang tính tham khảo**, không thay thế bác sĩ.
- Luôn hiển thị cảnh báo này cho người dùng khi deploy.
- Không lưu trữ thông tin y tế của người dùng khi không có sự đồng ý.
