from PyPDF2 import PdfReader
import time
sum = 0

pdf_path = "resources/Munamadan1Page (PDF1).pdf"

for i in range(100):
    start = time.time()
    reader = PdfReader(pdf_path)
    page = reader.pages[0] #page number as index
    page.extract_text()
    end = time.time()
    sum += (end - start)
    print(end - start)

print("Avg time of 100", sum/100)
# print(len(page.extract_text()))
# print(page.extract_text())
