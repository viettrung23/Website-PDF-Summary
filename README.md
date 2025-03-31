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

## Hướng dẫn cài đặt
1. **Clone repository**:
   ```bash
   git clone https://github.com/viettrung23/Website-PDF-Summary.git
   cd Website-PDF-Summary
2. **Tạo môi trường ảo**
    ```bash
    python -m venv venv
    venv\Scripts\activate
3. **Cài đặt thư viện**
    ```bash
    pip install -r requirements.txt
4. **Cài đặt Tesseract OCR**
- Tải [tesseract-ocr-w64-setup-5.5.0.20241111.exe](https://github.com/UB-Mannheim/tesseract/wiki) (64 bit)
- Cài đặt biến môi trường
5. **Cài đặt Poppler**
- Tải [Release-24.08.0-0.zip](https://github.com/oschwartz10612/poppler-windows/releases)
- Cài đặt biến môi trường
6. **Thực thi code**
    ```bash
    streamlit run app.py

