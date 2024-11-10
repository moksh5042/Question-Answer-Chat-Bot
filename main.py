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

st.title("Answer Evaluator")

# Sidebar
with st.sidebar:
    question_text = st.text_area("Question Text")
    st.write("OR")
    question_image = st.file_uploader("Image of Question")
    answer_text = st.text_area("Answer Text")
    st.write("OR")
    answer_image = st.file_uploader("Image of Answer")
    
    # answer_type = st.selectbox("Type of Answer", ["MCQ", "Long Answer", "Short Answer"])


if question_image and question_text:
    st.error("Shi data daal")

if answer_image and answer_text:
    st.error("Shi data daal")


def llm_output(qus_text, ans_text,total_marks):
    print("text",qus_text, ans_text,total_marks)
    template = """You are an answer evaluator responsible for grading a student's response to a question. Your task is to assign a score from 1 to {total_marks} based on the accuracy, relevance, and completeness of the student's answer. 

IMPORTANT: Provide only the numeric score as your response, with no additional text or commentary.

Question: {ques_text}

Student Answer: {stud_ans_text}"""
    

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    res = chain.invoke({"ques_text": qus_text,
                        "stud_ans_text": ans_text,
                        "total_marks":total_marks})
    # print
    
    # print("llm",res)
    # st.markdown("test")
    return res
    

# Main Content
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
        # st.write("OCR genrated text of question")
        # st.write(qus_text)

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


        st.markdown('''
        ## OCR genrated text: ''')
        # st.write(ans_text)
        # st.write(f"##### {qus_text}")
        # st.write(f"##### {ans_text}")
        st.write(f'''    {qus_text}''')
        st.write(f'''    {ans_text}''')


else:
    qus_text = question_text
    ans_text = answer_text

with st.form("my_form"):
    marks_text = st.text_area("maximun marks? :", "10")
    submitted = st.form_submit_button("Submit")
    # st.write(marks_text)
    # print("marks input",marks_text,submitted)

if st.button("Run"):
    res = llm_output(qus_text=qus_text,
                        ans_text=ans_text,
                        total_marks=marks_text)
    st.write(f"Marks Obtain by student out of {marks_text}")
    st.write(res)
        
        