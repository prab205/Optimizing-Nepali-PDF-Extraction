import easyocr
import fitz
import time
sum = 0
avg = 0

reader = easyocr.Reader(['ne','en']) # this needs to run only once to load the model into memory

for i in range(100):
    start = time.time()
    doc = fitz.open("resources/Munamadan1Page (PDF1).pdf")
    page = doc[0]
    #1,1 stands for zoom_x,zoom_y. Higher zoom clear text, unclear images i.e. amplifies noise
    mat = fitz.Matrix(2,2)

    pix = page.get_pixmap(matrix= mat, alpha=False)
    pix.save(f"resources/images/Temp_Image_{i}.png")

    result = reader.readtext(f'resources/images/Temp_Image_{i}.png', detail = 0)

    if i==0:
        print(result)

    end = time.time()
    print(end - start)
    sum += end - start
    print(f"Avg is {float(sum)/float(i+1)}")

print("Avg time of 100 is ",sum/100)
