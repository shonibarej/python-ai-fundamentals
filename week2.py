import numpy as np

# v1 = np.array([1,2,3,4,5])
# v2 = np.array([10,20,30,40,50])

# # Basic operations — applied to every element at once:
# print(v1+v2)
# print(v1*2)
# print(v1**2)

# # Shape and type:

# print(v1.shape)
# print(v1.dtype)

# # 2D array — a matrix:
# matrix = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(matrix.shape)
# print(matrix[0])
# print(matrix[1][2])

# def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
#     dot_product = np.dot(a,b)
#     norm_a = np.linalg.norm(a)
#     norm_b = np.linalg.norm(b)
#     return dot_product / (norm_a * norm_b)

# # Test with simple vectors:
# v1 = np.array([1.0, 0.0, 0.0])  # points right
# v2 = np.array([1.0, 0.0, 0.0])  # same direction
# v3 = np.array([0.0, 1.0, 0.0])  # points up
# v4 = np.array([-1.0, 0.0, 0.0]) # opposite direction

# print(cosine_similarity(v1, v2))  # identical
# print(cosine_similarity(v1, v3))  # perpendicular
# print(cosine_similarity(v1, v4))  # opposite

# Fake embeddings — 4 dimensional vectors:
documents = {
    "Python is great for AI": np.array([0.9, 0.1, 0.2, 0.1]),
    "LangChain simplifies LLMs": np.array([0.8, 0.2, 0.1, 0.1]),
    "Power BI is used in UK": np.array([0.1, 0.9, 0.1, 0.2]),
    "SQL is great for data": np.array([0.1, 0.8, 0.2, 0.1]),
    "FastAPI builds REST APIs": np.array([0.7, 0.1, 0.8, 0.1]),   
}

query = np.array([0.85, 0.1, 0.15, 0.1])

def vector_search(query: np.ndarray, documents: dict) -> list[tuple[str, float]]:
    result = []
    norm_query = np.linalg.norm(query)
    for doc, embeddings in documents.items():
        norm_document = np.linalg.norm(embeddings)
        dot_product = np.dot(query, embeddings)
        similarity = dot_product / (norm_query * norm_document)
        result.append((doc, similarity))
    result.sort(key=lambda x:x[1], reverse = True)

    return result[:3]
    

print(vector_search(query, documents))

results = vector_search(query, documents)
for doc, score in results:
    print(f"{score:.3f} — {doc}")