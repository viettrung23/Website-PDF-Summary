import ollama
from config.constants import MODEL, SYSTEM_PROMPT
from models.website import Website
from services.pdf_reader import PDFDocument
import logging

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
            raise ValueError("Đầu vào không hợp lệ: cần URL hoặc file PDF")

        # Tạo prompt
        prompt = (
            f"Extract the main content from the {source_type} titled '{content.title}'. "
            "Ignore navigation menus, footers, ads, and sidebars if any. "
            "Summarize the essential information, including news or announcements, in markdown format.\n\n"
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