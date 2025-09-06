from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

class Person(BaseModel):
    name : str= Field(description='name of the person indian')
    age : int=Field(description='gt 18 and st 80 , this it rhe age of the person')
    city:str = Field(description='name of the city in which the person lives')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='generate the name , age , city of a fictional person in {format_instruction}' ,
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.format()

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
print(type(final_result))