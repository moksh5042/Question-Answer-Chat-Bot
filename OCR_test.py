from paddleocr import PaddleOCR

ocr = PaddleOCR()

# print(ocr.ocr("./img1.png"))

# b=[[[[[15.0, 11.0], [663.0, 10.0], [663.0, 28.0], [15.0, 29.0]], ('Q.A car moves with a speed of 40km/hr for15 minutes and then with a speed of 60km/hr', 0.9655373692512512)], [[[14.0, 31.0], [668.0, 33.0], [668.0, 52.0], [14.0, 49.0]], ('for the next 15 minutes.What is the total distance covered by the car?Also,find the average', 0.9857889413833618)], [[[16.0, 57.0], [218.0, 57.0], [218.0, 72.0], [16.0, 72.0]], ('speed of the car. [5 MARKS]', 0.9578235149383545)]]]
b=ocr.ocr("./q1_a.png")
print(b)
for x in b[0]:
    print(x[1][0],end=" ")

