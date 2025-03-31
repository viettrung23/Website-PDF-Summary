import pdfplumber
from pdf2image import convert_from_bytes
import pytesseract
import logging

logger = logging.getLogger(__name__)

# Cấu hình Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-24.08.0\Library\bin"

class PDFDocument:
    def __init__(self, file):
        """Khởi tạo PDFDocument và trích xuất nội dung từ file PDF."""
        self.title = file.name
        self.text = ""
        logger.info(f"Xử lý PDF: {self.title}")
        self._extract_content(file)

    def _extract_content(self, file) -> None:
        """Trích xuất văn bản, bảng hoặc OCR từ PDF."""
        try:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    self.text += self._get_page_content(page, file) or ""
                if not self.text.strip():
                    logger.error("Không có nội dung nào được trích xuất")
                    raise ValueError("No text or tables could be extracted from the PDF.")
            logger.info(f"Hoàn tất: {len(self.text)} ký tự")
        except Exception as e:
            logger.error(f"Lỗi xử lý PDF: {e}")
            raise ValueError(f"Error processing PDF: {e}")

    def _get_page_content(self, page, file) -> str:
        """Trích xuất nội dung từ một trang PDF."""
        # Thử trích xuất văn bản trực tiếp
        text = page.extract_text(layout=True, x_tolerance=2, y_tolerance=2)
        if text:
            return text + "\n\n"

        logger.warning(f"Không có văn bản ở trang {page.page_number}, thử OCR")
        # Thử OCR nếu không có văn bản
        ocr_text = self._try_ocr(page, file)
        if ocr_text:
            return ocr_text + "\n\n"

        # Thử trích xuất bảng
        return self._extract_tables(page)

    def _try_ocr(self, page, file) -> str:
        """Thử OCR cho một trang nếu cần."""
        try:
            file.seek(0)
            images = convert_from_bytes(
                file.read(),
                first_page=page.page_number,
                last_page=page.page_number,
                poppler_path=POPPLER_PATH
            )
            ocr_text = pytesseract.image_to_string(images[0])
            logger.info(f"OCR thành công cho trang {page.page_number}")
            return ocr_text
        except Exception as e:
            logger.error(f"OCR thất bại cho trang {page.page_number}: {e}")
            return ""

    def _extract_tables(self, page) -> str:
        """Trích xuất bảng từ trang nếu có."""
        tables = page.extract_tables()
        if not tables:
            return ""
        table_text = "\n".join(" | ".join(str(cell) for cell in row if cell) for table in tables for row in table)
        return table_text + "\n"