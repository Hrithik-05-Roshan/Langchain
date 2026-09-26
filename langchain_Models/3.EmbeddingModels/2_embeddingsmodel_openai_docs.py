from openai import embeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model= "text-embeddings-3-large", dimensions=32)

Document = [
    "Delhi is main city",
    "kolkata is our next target",
    "Hydrabad is crowded enough to target"
]

result = embeddings.embed_documents(Document)

print(str(result))
