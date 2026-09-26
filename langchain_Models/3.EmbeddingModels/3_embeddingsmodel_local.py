from torch._functorch._aot_autograd.logging_utils import model_name
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name= "HuggingFaceTB/SmolLM2-135M-Instruct")

Document = [
    "Delhi is main city",
    "kolkata is our next target",
    "Hydrabad is crowded enough to target"
]

result = embeddings.embed_documents(Document)

print(str(result))
