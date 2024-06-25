import aiofiles
import fitz  # PyMuPDF

async def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    async with aiofiles.open(pdf_path, 'rb') as file:
        pdf_content = await file.read()

    pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text
