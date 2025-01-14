import os
from chromadb.utils.embedding_functions import GoogleVertexEmbeddingFunction

embedder = GoogleVertexEmbeddingFunction(model_name="text-embedding-005",
                                         project_id="bio-llm",
                                         region="asia-northeast3",
                                         api_key=os.getenv("GOOGLE_API_KEY"))
embedder(["Hello, world!"])
