from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Annotated, TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

class Review(TypedDict):
    summary:Annotated[str , "a brief summary of the reviwe"]
    sentiment:Annotated[str , ' a positive or negative review']

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("Despite the devices impressive marketing promises, the actual experience has been frustratingly poor. The operating system feels sluggish, riddled with bugs that cause frequent crashes, and the constant overheating makes even simple tasks unbearable. The pre-installed apps are not only useless but also impossible to remove, cluttering the interface and draining storage. Customer support was dismissive, offering no meaningful solutions, and the battery life has deteriorated rapidly within just a few weeks. Overall, this product feels rushed, unfinished, and unworthy of its premium price tag.")

print(result)
