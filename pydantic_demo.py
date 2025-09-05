from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

load_dotenv()

# model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")


class Student(BaseModel):
    name:str


new_student = Student(name='sai')

print(type(new_student))
