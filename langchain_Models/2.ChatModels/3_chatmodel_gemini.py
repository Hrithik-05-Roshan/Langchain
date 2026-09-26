from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

result=model.invoke("what is the result of 2+3?")
# print(result.content)
print(result.content[0]["text"])
