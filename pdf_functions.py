import fitz  # PyMuPDF
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Merge PDFs
def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

# Split PDF (by pages)
def split_pdf(input_pdf, output_folder):
    pdf = PdfReader(input_pdf)
    for i, page in enumerate(pdf.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = f"{output_folder}/page_{i+1}.pdf"
        with open(output_path, "wb") as f:
            writer.write(f)

# Rotate pages
def rotate_pdf(input_pdf, output_pdf, angle=90):
    pdf = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in pdf.pages:
        page.rotate(angle)
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)

# Extract pages
def extract_pages(input_pdf, output_pdf, pages):
    pdf = PdfReader(input_pdf)
    writer = PdfWriter()
    for i in pages:
        writer.add_page(pdf.pages[i])
    with open(output_pdf, "wb") as f:
        writer.write(f)

# Add text overlay
def add_text(input_pdf, output_pdf, text, x=50, y=50, fontsize=12):
    doc = fitz.open(input_pdf)
    for page in doc:
        page.insert_text((x, y), text, fontsize=fontsize, color=(0,0,0))
    doc.save(output_pdf)

# Add image
def add_image(input_pdf, output_pdf, image_path, x=50, y=50, width=None, height=None):
    doc = fitz.open(input_pdf)
    for page in doc:
        rect = fitz.Rect(x, y, x + (width or 100), y + (height or 100))
        page.insert_image(rect, filename=image_path)
    doc.save(output_pdf)

# Highlight text
def highlight_text(input_pdf, output_pdf, search_text):
    doc = fitz.open(input_pdf)
    for page in doc:
        text_instances = page.search_for(search_text)
        for inst in text_instances:
            page.add_highlight_annot(inst)
    doc.save(output_pdf)
