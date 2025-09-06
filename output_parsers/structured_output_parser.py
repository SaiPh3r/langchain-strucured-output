from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema


load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

schema = [
    ResponseSchema(name='fact1' , description='fact 1 about the topic') , 
    ResponseSchema(name='fact2' , description='fact 2 about the topic') ,
    ResponseSchema(name='fact3' , description='fact 3 about the topic') ,

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='write 3 facts about {topic} in {format}' , 
    input_variables=['topic'] ,
    partial_variables={'format':parser.get_format_instructions()}
)


prompt = template.invoke({'topic':'black-hole'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)


