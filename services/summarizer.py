import ollama
from config.constants import MODEL, SYSTEM_PROMPT
from models.website import Website
from models.pdf_reader import PDFDocument
import logging

# Thiết lập cấu hình logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def summarize(content):
    """Tóm tắt nội dung từ URL hoặc file PDF thành markdown."""
    try:
        # Xử lý đầu vào
        if isinstance(content, str):  # URL
            logger.info(f"Xử lý URL: {content}")
            content = Website(content)
            source_type = "website"
        elif hasattr(content, 'read'):  # File PDF
            logger.info(f"Xử lý PDF: {content.name}")
            content = PDFDocument(content)
            source_type = "document"
        else:
            logger.error("Đầu vào không hợp lệ")
            raise ValueError("Đầu vào không hợp lệ: cần URL hoặc file PDF")

        # Tạo prompt
        logger.debug("Tạo prompt cho mô hình")
        prompt = (
            f"Extract the main content from the {source_type} titled '{content.title}'. "
            "Ignore navigation menus, footers, ads, and sidebars if any. "
            "Summarize the essential information, including news, announcements, tables, and mathematical formulas, in markdown format. "
            "For tables, present them in markdown table syntax. For formulas, use LaTeX notation where applicable.\n\n"
            f"{content.text}"
        )

        # Gửi yêu cầu tới mô hình
        logger.debug(f"Gửi yêu cầu đến {MODEL}")
        response = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]
        )
        logger.info("Tóm tắt hoàn tất")
        return response['message']['content']

    except Exception as e:
        logger.error(f"Lỗi tóm tắt: {e}")
        return f"An error occurred: {e}"