from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="clause-3.5-sonnes-20227902")

result=model.invoke("what is the result of 2+3?")
print(result.invoke)