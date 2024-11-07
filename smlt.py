import streamlit as st
import os
import uuid

BASE_FOLDER = os.getcwd()


# Sidebar
with st.sidebar:
    question_text = st.text_area("Question Text")
    question_image = st.file_uploader("Image of Question")
    answer_text = st.text_area("Answer Text")
    answer_image = st.file_uploader("Image of Answer")
    answer_type = st.selectbox("Type of Answer", ["MCQ", "Long Answer", "Short Answer"])

# Main Content
st.title("Answer Evaluator")

if question_image:
    image_name = os.path.join(BASE_FOLDER, str(uuid.uuid4())+'.jpg')
    with open(image_name,"wb") as f:
        f.write(question_image.getvalue())

if answer_image:
    image_name = os.path.join(BASE_FOLDER, str(uuid.uuid4())+'.jpg')
    with open(image_name,"wb") as f:
        f.write(answer_image.getvalue())

# if question_text:

# if image_upload is not None:
#     st.image(image_upload, caption="Image of Question")

# if answer_upload is not None:
#     st.image(image_upload, caption="Image of Answer")

# if answer_text:
#     st.write("**Answer Text:**", answer_text)

# if answer_type:
#     st.write("**Type of Answer:** ", answer_type)

# if st.button("Run"):
#     # Evaluate the answer and display the results
#     total_marks = 10
#     topic = "Mathematics"
#     st.write("**Total Marks:** ", total_marks)
#     st.write("**Topic:** ", topic)