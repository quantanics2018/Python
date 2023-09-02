import PyPDF2

# Open the PDF file
with open('document.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Get the number of pages
    num_pages = len(pdf_reader.pages)
    print("Number of pages:", num_pages)
    
    # Extract text from a specific page
    page_text = pdf_reader.pages[0].extract_text()
    print("Text from first page:", page_text)
