from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel , Field
from typing import Literal
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

class Review(BaseModel):
    summary : str = Field(description= "a brief summary of the reviwe") 
    sentiment : Literal['pos' , 'neg'] = Field(description= "a positive or negative review")


structure_model = model.with_structured_output(Review)

result = structure_model.invoke("Despite the devices impressive marketing promises, the actual experience has been frustratingly poor. The operating system feels sluggish, riddled with bugs that cause frequent crashes, and the constant overheating makes even simple tasks unbearable. The pre-installed apps are not only useless but also impossible to remove, cluttering the interface and draining storage. Customer support was dismissive, offering no meaningful solutions, and the battery life has deteriorated rapidly within just a few weeks. Overall, this product feels rushed, unfinished, and unworthy of its premium price tag.")

print(result)