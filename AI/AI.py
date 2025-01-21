from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

TEMPLATE = """
Ответьте на вопрос ниже. 

Вот история разговора: {context}

Вопрос: {question}

Ответ:
"""

model = OllamaLLM(model="mistral-nemo")
promt = ChatPromptTemplate.from_template(TEMPLATE)
chain = promt | model


def handle_conversation(user_input, context0):
    result = chain.invoke({"context": context0, "question": user_input})
    context = context0 + f"\nUser: {user_input}\nAi: {result}"
    return result, context
