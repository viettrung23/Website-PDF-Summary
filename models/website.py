import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class Website:
    def __init__(self, url: str):
        """Khởi tạo đối tượng Website từ URL và trích xuất nội dung chính."""
        self.url = url
        self.title = "No title found"
        self.text = ""
        self._scrape_content()

    def _scrape_content(self) -> None:
        """Thu thập và xử lý nội dung từ URL."""
        logger.info(f"Đang thu thập dữ liệu từ: {self.url}")
        html_content = self._fetch_html()
        if html_content:
            self._parse_html(html_content)

    def _fetch_html(self) -> bytes | None:
        """Tải nội dung HTML từ URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            logger.error(f"Lỗi khi tải URL {self.url}: {e}")
            raise

    def _parse_html(self, html_content: bytes) -> None:
        """Phân tích HTML và trích xuất tiêu đề cùng nội dung chính."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Lấy tiêu đề
        self.title = soup.title.string if soup.title else "No title found"
        logger.info(f"Tiêu đề: {self.title}")

        # Loại bỏ các phần không cần thiết và lấy nội dung
        if soup.body:
            for tag in soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
            logger.debug(f"Đã trích xuất {len(self.text)} ký tự")