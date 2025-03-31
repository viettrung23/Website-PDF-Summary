# Website & PDF Summary App

Ứng dụng này cho phép người dùng tóm tắt nội dung chính từ một website hoặc file PDF bằng cách sử dụng API Ollama với mô hình `llama3.2`. Nó tự động loại bỏ các phần không cần thiết như menu điều hướng, quảng cáo, sidebar, footer và trả về bản tóm tắt ngắn gọn dưới dạng Markdown.

## Tính năng
- Tóm tắt nội dung từ URL website.
- Tóm tắt nội dung từ file PDF (bao gồm văn bản, bảng, và OCR cho PDF dạng ảnh).
- Giao diện đơn giản với Streamlit.
- Log chi tiết quá trình xử lý.

## Công nghệ sử dụng
- **Python**: Ngôn ngữ chính.
- **Streamlit**: Giao diện người dùng.
- **Ollama**: API tóm tắt với mô hình `llama3.2`.
- **BeautifulSoup**: Trích xuất nội dung website.
- **pdfplumber & pdf2image**: Xử lý PDF.
- **pytesseract**: OCR cho PDF dạng ảnh.
- **requests**: Tải nội dung từ URL.

## Cấu hình
- Python 3.8+
- Git
- Tesseract OCR (cho PDF dạng ảnh)
- Poppler (cho `pdf2image`)

