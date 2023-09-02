import PyPDF2

pdf_writer = PyPDF2.PdfWriter()

with open('doo.pdf', 'rb') as pdf1, open('re.pdf', 'rb') as pdf2:
    pdf_reader1 = PyPDF2.PdfReader(pdf1)
    pdf_reader2 = PyPDF2.PdfReader(pdf2)
    
    for page in pdf_reader1.pages:
        pdf_writer.add_page(page)
    for page in pdf_reader2.pages:
        pdf_writer.add_page(page)
    
    with open('merged.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)
