import os
import time
from PyPDF2 import PdfReader, PdfWriter

# Function to split the PDF file
def split_pdf(file_path, max_size_mb):
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    
    output_file_count = 1
    output_pdf = PdfWriter()
    output_file_name = lambda count: f"part_{count}.pdf"
    current_file_pages = 0

    print(f'Total pages: {total_pages}')


    for page_number in range(total_pages):

        output_pdf.add_page(reader.pages[page_number])
        current_file_pages += 1
        
        with open(output_file_name(output_file_count), "wb") as temp_file:
            output_pdf.write(temp_file)
        
        output_file_size = os.path.getsize(output_file_name(output_file_count)) / (1024 * 1024)

        print(f'Output file size: {output_file_size:.2f} MB')
        
        if output_file_size > max_size_mb:
            output_file_count += 1
            output_pdf = PdfWriter()
            output_pdf.add_page(reader.pages[page_number])
            current_file_pages = 1

            print(f'Output file count: {output_file_count}')
            time.sleep(1)

    with open(output_file_name(output_file_count), "wb") as output_file:
        output_pdf.write(output_file)

split_pdf("sample.pdf", 49)
