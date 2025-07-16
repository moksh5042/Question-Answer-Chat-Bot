# Initialize PaddleOCR instance
from paddleocr import PaddleOCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

# Run OCR inference on a sample image 
result = ocr.predict(
    input=r"/home/moksh/Desktop/ind_project/Question-Answer-Chat-Bot/img1.png")
# print(result)
a=result
print(a[0]["rec_texts"][0])

qus_text=""
    # print(question_ocr)
# # print(result["rec_texts"])
# for x in result[0]:
#     # print(x[1][0],end=" ")
#     if (x=="rec_texts"):
#         print(result[0][x])
        # print(result["rec_texts"])
    # qus_text+=x[1][0]
    # qus_text+=" "    

# Visualize the results and save the JSON results
# for res in result:
#     res.print()
#     res.save_to_img("output")
#     res.save_to_json("output")
