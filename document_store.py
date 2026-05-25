# class DocumentStore:
#     def __init__(self):
#         self.document = []

#     def add(self, doc: str) -> None:
#         self.document.append(doc)

#     def search(self, query:str) -> list[str]:
#         return [doc for doc in self.document if query in doc]

#     def __len__(self) -> int:
#         return len(self.document)

#     def __repr__(self) -> str:
#         documentstored = len(self.document)
#         return f"Documents stored {documentstored} documents"
    

# class RankedDocumentStore(DocumentStore):
#     def search(self, query: str) -> list[str]:
#         result = sorted([doc for doc in self.document if query in doc.split()],
#                key=lambda doc: doc.split().count(query), reverse=True)
#         return result
        
    
# ranked_store = RankedDocumentStore()
# ranked_store.add("Python is great for AI engineering")
# ranked_store.add("Python and Python are used everywhere")
# ranked_store.add("LangChain simplifies LLM development")
# ranked_store.add("Python is also used for data analysis")

# print(ranked_store.search("Python"))



# from abc import ABC, abstractmethod

# class BaseRetriever(ABC):
    
#     @abstractmethod
#     def retrieve(self, query: str) -> list[str]:
#         pass
    
#     def describe(self):
#         print(f"I am a {self.__class__.__name__}")


# class VectorRetriever(BaseRetriever):
#     def __init__(self, documents: list[str]):
#         self.documents = documents

#     def retrieve(self,query:str) -> list[str]:
#         return [doc for doc in self.documents if query in doc ]
    

# class BrokenRetriever(BaseRetriever):
#     def __init__(self):
#         pass


# broken = BrokenRetriever()
    

# retriever = VectorRetriever(["Python is great", "LangChain is powerful"])
# retriever.describe()
# print(retriever.retrieve("Python"))

#writing a file
# with open("note.txt", "w") as f:
#     f.write("Python is great for AI\n")
#     f.write("Langchain simplifies LLM development\n")
#     f.write("Power BI is used in UK enterprises\n")


# #Reading the whole file
# with open("note.txt", "r") as f:
#     content = f.read()
#     print(content)

#Read line by line
# with open("note.txt", "r") as f:
#     for line in f:
#         print(line.strip())


# Append to existing file:
# with open("note.txt", "a") as f:
#     f.write("RAG systems are powerful\n")

# Read the whole file again:
# with open("note.txt", "r") as f:
#     print(f.read())
import json
import os

def save_results(data: list[dict], path: str ) -> int:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return len(data)

def load_results(path:str):
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
            return data
    else:
        return []
    

results = [
    {"question": "What is RAG?", "answer": "Retrieval Augmented Generation"},
    {"question": "What is LangChain?", "answer": "A framework for LLMs"}
]

count = save_results(results, "results.json")
print(f"Saved {count} items")

loaded = load_results("results.json")
print(loaded)

# Test empty list for missing file:
print(load_results("missing.json"))
        
        
