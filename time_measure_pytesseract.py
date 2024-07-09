import fitz
import pytesseract
import time
sum = 0

for i in range(100):
    start = time.time()
    pytesseract.pytesseract.tesseract_cmd = r'resources\Tesseract-OCR\tesseract.exe'
    doc = fitz.open("resources/Ghumne Mech-8 (PDF2).pdf")
    page = doc[0]
    #1,1 stands for zoom_x,zoom_y. Higher zoom clear text, unclear images i.e. amplifies noise
    mat = fitz.Matrix(1,1)

    pix = page.get_pixmap(matrix= mat, alpha=False)
    pix.save("resources/images/Temp_Image.png")

    pytesseract.image_to_string("resources/images/Temp_Image.png", 'Devanagari')
    end = time.time()
    #print(pytesseract.image_to_string("Temp_Image.png", 'Devanagari'))
    print(end - start)
    sum += end - start
    print(f'Avg is {sum/float(i+1)}')

print("Avg time of 100 is ", sum/100)