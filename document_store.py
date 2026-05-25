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
    
store = DocumentStore()
store.add("Python is great for AI engineering")
store.add("LangChain simplifies LLM development")
store.add("Power BI is widely used in UK enterprises")
store.add("Python is also used for data analysis")

print(store)                    # tests __repr__
print(len(store))               # tests __len__
print(store.search("Python"))   # should return 2 documents
print(store.search("LangChain")) # should return 1 document
print(store.search("Java"))     # should return empty list