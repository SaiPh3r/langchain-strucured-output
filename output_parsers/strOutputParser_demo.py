from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


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

parser = StrOutputParser()

chain = template1 | model | parser | template2  | model | parser

result = chain.invoke({'topic':'black-hole'})

print(result)