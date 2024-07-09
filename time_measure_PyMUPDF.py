import fitz
import time
sum = 0

pdf_path = "resources/Ghumne Mech-8 (PDF2).pdf"

for i in range(100):
    start = time.time()
    doc = fitz.open(pdf_path)
    doc.get_page_text(0)
    end = time.time()
    sum += (end - start)
    print(end - start)

text = doc.get_page_text(0)
print("Avg time of 100 is ", sum/100)
# print(len(text))
# print(text)
