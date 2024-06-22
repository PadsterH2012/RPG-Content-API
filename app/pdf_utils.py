import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def process_uploaded_pdfs(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            print(f"Extracted text from {filename}:")
            print(text)
            print("\n" + "-"*50 + "\n")

# Example usage
if __name__ == "__main__":
    pdf_directory = 'uploaded_pdfs'
    process_uploaded_pdfs(pdf_directory)
