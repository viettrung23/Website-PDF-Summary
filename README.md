
# Website & PDF Summary App

## Tổng quan

Ứng dụng này cho phép người dùng tóm tắt nội dung chính từ các trang web hoặc file PDF một cách nhanh chóng và hiệu quả. Nó tập trung vào việc trích xuất thông tin cốt lõi, loại bỏ các phần không cần thiết như menu điều hướng, quảng cáo, hoặc chân trang, và trình bày kết quả dưới dạng Markdown rõ ràng, dễ đọc.

### Tính năng chính
- **Tóm tắt từ URL**: Nhập URL của một trang web để trích xuất và tóm tắt nội dung chính.
- **Tóm tắt từ PDF**: Tải lên file PDF để phân tích và tóm tắt nội dung.
- **Định dạng đầu ra**: Kết quả được trình bày dưới dạng Markdown, hỗ trợ bảng (Markdown table syntax) và công thức toán học (LaTeX notation).
- **Loại bỏ nội dung không cần thiết**: Bỏ qua quảng cáo, menu, sidebar, footer để tập trung vào thông tin quan trọng.
- **Giao diện thân thiện**: Sử dụng Streamlit để cung cấp giao diện người dùng đơn giản với hai tab riêng biệt cho website và PDF.

## Công nghệ sử dụng
- **Python**: Ngôn ngữ lập trình chính.
- **Streamlit**: Framework để xây dựng giao diện web tương tác.
- **BeautifulSoup**: Phân tích và trích xuất nội dung từ HTML của trang web.
- **LlamaParse**: Công cụ trích xuất văn bản, bảng và công thức từ file PDF (sử dụng API từ Llama Cloud).
- **Ollama**: Mô hình AI (`llama3.2`) để tóm tắt nội dung.
- **Requests**: Gửi yêu cầu HTTP để tải nội dung trang web.
- **Logging**: Theo dõi và ghi lại quá trình xử lý để debug và giám sát.
- **python-dotenv**: Quản lý biến môi trường (ví dụ: API key).

## Hướng dẫn cài đặt

### 1. Sao chép repository
Clone repository về máy của bạn:
```bash
git clone https://github.com/viettrung23/Website-PDF-Summary.git
cd Website-PDF-Summary
```

### 2. Cài đặt môi trường ảo (khuyến nghị)
Tạo một môi trường ảo để cách ly các thư viện của dự án với hệ thống:
```bash
python -m venv venv
```
Kích hoạt môi trường ảo:
- Trên Linux hoặc Mac:
  ```bash
  source venv/bin/activate
  ```
- Trên Windows:
  ```bash
  venv\Scripts\activate
  ```
Khi môi trường ảo được kích hoạt, bạn sẽ thấy `(venv)` xuất hiện trước dấu nhắc lệnh trong terminal.

### 3. Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### 4. Cấu hình biến môi trường
Tạo một file `.env` trong thư mục gốc của dự án và thêm API key của bạn:
```
LLAMA_API_KEY=<YOUR_API_KEY>
```
- Thay `<YOUR_API_KEY>` bằng khóa API thực tế từ Llama Cloud.
- File `.env` sẽ được tự động đọc bởi `python-dotenv` khi ứng dụng khởi chạy.

### 5. Chạy ứng dụng
Khởi động ứng dụng bằng lệnh:
```bash
streamlit run app.py
```
- Sau khi chạy, Streamlit sẽ hiển thị URL (thường là `http://localhost:8501`).
- Mở trình duyệt và truy cập URL này để sử dụng ứng dụng.
