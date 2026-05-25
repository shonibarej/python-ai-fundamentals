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



from abc import ABC, abstractmethod

class BaseRetriever(ABC):
    
    @abstractmethod
    def retrieve(self, query: str) -> list[str]:
        pass
    
    def describe(self):
        print(f"I am a {self.__class__.__name__}")


class VectorRetriever(BaseRetriever):
    def __init__(self, documents: list[str]):
        self.documents = documents

    def retrieve(self,query:str) -> list[str]:
        return [doc for doc in self.documents if query in doc ]
    

class BrokenRetriever(BaseRetriever):
    def __init__(self):
        pass


broken = BrokenRetriever()
    

retriever = VectorRetriever(["Python is great", "LangChain is powerful"])
retriever.describe()
print(retriever.retrieve("Python"))