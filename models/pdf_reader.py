from llama_parse import LlamaParse
from config.constants import LLAMA_API_KEY
import logging
import tempfile
import os

# Thiết lập cấu hình logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

class PDFDocument:
    def __init__(self, file):
        """Khởi tạo PDFDocument và trích xuất nội dung từ file PDF bằng LlamaParse."""
        self.title = file.name
        self.text = ""
        logger.info(f"Xử lý PDF: {self.title}")
        self._extract_content(file)

    def _extract_content(self, file) -> None:
        """Trích xuất văn bản từ PDF bằng LlamaParse."""
        try:
            # Lưu tạm file PDF từ streamlit file_uploader
            logger.debug("Lưu file PDF tạm thời")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(file.read())
                tmp_file_path = tmp_file.name
                logger.debug(f"Đã lưu file tạm tại: {tmp_file_path}")

            # Khởi tạo LlamaParse
            logger.debug("Khởi tạo LlamaParse")
            parser = LlamaParse(
                api_key=LLAMA_API_KEY,
                result_type="markdown",
                parsing_instruction="Extract text, tables, and mathematical formulas where possible."
            )

            # Đọc file PDF
            logger.debug(f"Bắt đầu trích xuất nội dung từ {tmp_file_path}")
            documents = parser.load_data(tmp_file_path)
            self.text = "\n".join(doc.text for doc in documents)
            
            if not self.text.strip():
                logger.error("Không có nội dung nào được trích xuất")
                raise ValueError("No text could be extracted from the PDF.")
            logger.info(f"Hoàn tất trích xuất: {len(self.text)} ký tự")

            # Xóa file tạm
            logger.debug(f"Xóa file tạm: {tmp_file_path}")
            os.unlink(tmp_file_path)
        except Exception as e:
            logger.error(f"Lỗi xử lý PDF: {e}")
            raise ValueError(f"Error processing PDF: {e}")