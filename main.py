from paddleocr import PaddleOCR
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import os
import uuid


ocr = PaddleOCR()
model = OllamaLLM(model="llama3.2:3b")

BASE_FOLDER = os.getcwd()
BASE_IMAGE_FOLDER = os.path.join(BASE_FOLDER,"Img")
os.makedirs(BASE_IMAGE_FOLDER,exist_ok=True)

# Sidebar
with st.sidebar:
    question_text = st.text_area("Question Text")
    question_image = st.file_uploader("Image of Question")
    answer_text = st.text_area("Answer Text")
    answer_image = st.file_uploader("Image of Answer")
    answer_type = st.selectbox("Type of Answer", ["MCQ", "Long Answer", "Short Answer"])

# Main Content
st.title("Answer Evaluator")

if question_image and answer_image:

    if question_image:
        st.image(question_image, caption="Image of Question")
        qus_image_name = os.path.join(BASE_IMAGE_FOLDER, str(uuid.uuid4())+'.jpg')
        with open(qus_image_name,"wb") as f:
            f.write(question_image.getvalue())
        question_ocr=ocr.ocr(qus_image_name)
        qus_text=""
        for x in question_ocr[0]:
            # print(x[1][0],end=" ")
            qus_text+=x[1][0]
            qus_text+=" "    
        # print(qus_text)
        st.write("OCR genrated text of question")
        st.write(qus_text)

    if answer_image:
        st.image(answer_image, caption="Image of Answer")
        ans_image_name = os.path.join(BASE_IMAGE_FOLDER, str(uuid.uuid4())+'.jpg')
        with open(ans_image_name,"wb") as f:
            f.write(answer_image.getvalue())    
        answer_ocr=ocr.ocr(ans_image_name)
        ans_text=""
        for x in answer_ocr[0]:
            # print(x[1][0],end=" ")
            ans_text+=x[1][0]
            ans_text+=" "
        # print(ans_text)
        st.write("OCR genrated text of answer")
        st.write(ans_text)

    if st.button("Run"):

        template = """You are a answer evaluator whose task is to evaluate the answer of the following question and give marks between 1 to 10.
IMPORTANT: Only return marks nothing else.

Question: {ques_text}

Student Answer: {stud_ans_text}"""

        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model
        res = chain.invoke({"ques_text": qus_text,
                            "stud_ans_text": ans_text})

        # print(res)
        st.markdown("test")
        st.write("Marks Obtain by student out of 10")
        st.write(res)