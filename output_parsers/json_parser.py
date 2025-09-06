from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate


load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template='give a random person fictional name , place where he lives , age  , sex of {format}' , 
    partial_variables={'format':parser.get_format_instructions()} 
)

prompt = template.format()

result = model.invoke(prompt)



final_result = parser.parse(result.content)
print(final_result)
print(type(final_result))


