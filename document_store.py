class DocumentStore:
    def __init__(self):
        self.document = []

    def add(self, doc: str) -> None:
        self.document.append(doc)

    def search(self, query:str) -> list[str]:
        return [doc for doc in self.document if query in doc]

    def __len__(self) -> int:
        return len(self.document)

    def __repr__(self) -> str:
        documentstored = len(self.document)
        return f"Documents stored {documentstored} documents"
    

class RankedDocumentStore(DocumentStore):
    def search(self, query: str) -> list[str]:
        result = sorted([doc for doc in self.document if query in doc.split()],
               key=lambda doc: doc.split().count(query), reverse=True)
        return result
        
    
ranked_store = RankedDocumentStore()
ranked_store.add("Python is great for AI engineering")
ranked_store.add("Python and Python are used everywhere")
ranked_store.add("LangChain simplifies LLM development")
ranked_store.add("Python is also used for data analysis")

print(ranked_store.search("Python"))