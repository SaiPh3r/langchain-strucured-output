from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

template1 = PromptTemplate(
    template= "write a detailed report on {topic}" , 
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="wtite a short 2 lines summary on text {text}" , 
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'langchain'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)

