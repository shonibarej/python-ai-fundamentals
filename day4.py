import csv

# data = [
#     {"name": "Alice", "role": "Data Analyst", "salary": 45000},
#     {"name": "Bob", "role": "AI Engineer", "salary": 75000},
#     {"name": "Carol", "role": "Data Analyst", "salary": 50000},
# ]

# with open("employees.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "role", "salary"])
#     writer.writeheader()
#     writer.writerows(data)


# with open("employees.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)

# with open("employees.csv", "r") as f:
#     reader = csv.DictReader(f)
#     analysts = [row for row in reader if row["role"] == "Data Analyst"]
#     print(analysts)

# class Document:
#     def __init__(self, id: str, content: str, source: str):
#         self.id = id
#         self.content = content
#         self.source = source


# from dataclasses import dataclass

# @dataclass
# class Documnent:
#     id: str
#     content: str
#     source: str


from dataclasses import dataclass, field
from datetime import datetime

# @dataclass
# class Document:
#     id: str
#     content: str
#     source: str
#     created_at: datetime = field(default_factory=datetime.utcnow)
#     tags: list = field(default_factory=list)


# doc1 = Document(id="1", content="Python is great for AI", source="manual")
# doc2 = Document(id="2", content="LangChain Simplifies LLMs", source="web", tags=["ai", "langchain"])

# print(doc1)
# print(doc2)
# print(doc1.content)
# print(doc2.tags)


