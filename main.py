from paddleocr import PaddleOCR
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import os
import uuid
from dotenv import load_dotenv

load_dotenv()


from groq import Groq

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)
print("OCR model loaded")   
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

def groq_llms(qus_text, ans_text, total_marks):
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages = [
    {
        "role": "system",
        "content": (
            f"You are a professional academic evaluator. Your task is to grade a student's answer based on the following criteria:\n"
            f"1. **Accuracy** – Is the answer factually and conceptually correct?\n"
            f"2. **Relevance** – Does the answer directly address the question and stay on topic?\n"
            f"3. **Completeness** – Does the answer fully cover the key points or expected elements?\n\n"
            f"Instructions:\n"
            f"- Assign an integer score between 1 and {total_marks}.\n"
            f"- Base your judgment solely on the quality of the answer in relation to the question.\n"
            f"- Do not consider grammar, spelling, or writing style unless it affects clarity.\n"
            f"- Respond with a **single integer only**, no comments or explanation.\n"
            f"- If the answer is blank, irrelevant, or completely wrong, give the lowest possible score.\n"
            f"- If the answer is perfect, complete, and well-aligned with the question, give full marks ({total_marks})."
        )
    },
    {
        "role": "user",
        "content": (
            f"Question:\n{qus_text.strip()}\n\n"
            f"Student's Answer:\n{ans_text.strip()}"
        )
    }
]

,
        temperature=0.2,
        max_tokens=1024,
        top_p=1,
        stop=None,
    )
    return completion.choices[0].message.content
        

# Main Content
if question_image and answer_image:

    if question_image:
        st.image(question_image, caption="Image of Question")
        # print("ok1")
        qus_image_name = os.path.join(BASE_IMAGE_FOLDER, str(uuid.uuid4())+'.png')
        # print(qus_image_name)
        with open(qus_image_name,"wb") as f:
            f.write(question_image.getvalue())
        question_ocr=ocr.predict(qus_image_name)
        qus_text=""
        # print(question_ocr[0]["rec_texts"][0])
        for x in question_ocr[0]["rec_texts"]:
            qus_text+=x
            qus_text+=" "

    if answer_image:
        st.image(answer_image, caption="Image of Answer")
        ans_image_name = os.path.join(BASE_IMAGE_FOLDER, str(uuid.uuid4())+'.jpg')
        with open(ans_image_name,"wb") as f:
            f.write(answer_image.getvalue())    
        answer_ocr=ocr.predict(ans_image_name)
        # ans_text=answer_ocr[0]["rec_texts"]
        # print("ans_text",ans_text)
        ans_text=""
        for y in answer_ocr[0]["rec_texts"]:
            ans_text+=y
            ans_text+=" "   



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
    res = groq_llms(qus_text=qus_text,
                        ans_text=ans_text,
                        total_marks=marks_text)
    st.write(f"Marks Obtain by student out of {marks_text}")
    st.write(res)
        
        