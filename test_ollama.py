from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# template = """Question: {question}

# Answer: Let's think step by step."""

template = """You are a answer evaluator whose task is to evaluate the answer of the following question and give marks between 1 to 10.

Question: {ques_text}

Student Answer: {stud_ans_text}"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2:3b")

chain = prompt | model

res = chain.invoke({"ques_text": "Who published the Human Development Index (HDI)?",
                    "stud_ans_text": "United Nations Development Programme (UNDP)."})

print(res)