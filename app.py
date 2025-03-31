import streamlit as st
from services.summarizer import summarize
import logging

logger = logging.getLogger(__name__)

def run_summary(content, content_type: str, spinner_text: str):
    """Chạy tóm tắt và hiển thị kết quả."""
    logger.info(f"Người dùng yêu cầu tóm tắt {content_type}: {content if isinstance(content, str) else content.name}")
    with st.spinner(spinner_text):
        summary = summarize(content)
    st.markdown(summary)

# Giao diện chính
st.title("Website & PDF Summary App")
st.markdown("Tóm tắt nội dung từ URL hoặc file PDF bằng Ollama API.")

# Tabs
tab1, tab2 = st.tabs(["Website", "PDF"])

# Tab Website
with tab1:
    url = st.text_input("Nhập URL:", "")
    if st.button("Tóm tắt", key="web_btn"):
        if url:
            run_summary(url, "URL", "Đang tóm tắt website...")
        else:
            logger.warning("Không có URL")
            st.warning("Vui lòng nhập URL hợp lệ.")

# Tab PDF
with tab2:
    pdf_file = st.file_uploader("Tải lên file PDF:", type=["pdf"])
    if st.button("Tóm tắt", key="pdf_btn"):
        if pdf_file:
            run_summary(pdf_file, "PDF", "Đang tóm tắt PDF...")
        else:
            logger.warning("Không có file PDF")
            st.warning("Vui lòng tải lên file PDF.")