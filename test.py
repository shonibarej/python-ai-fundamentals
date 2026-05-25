# word_count — how many words are in the text
# unique_word_count — how many different words (no duplicates)
# most_common_word — the word that appears most often
# avg_word_length — the average number of characters per word

# text= "This cat is the most the hansdome cat in the word"
# def analyse_text(text: str) -> dict:
#     result = {}
#     unique_word =[]
#     text_splitter = text.split()
#     word_count = len(text_splitter)
#     result["world_count"] = word_count
#     for word in text_splitter:
#         if word not in unique_word:
#             unique_word.append(word)
#     result["unique_word"] = len(unique_word)
#     avg_word_length = len(text)/len(text_splitter)
#     result["avg_word_length"] = avg_word_length
#     most_common_word = max(text_splitter, key = text_splitter.count)
#     result["most_common_word"] = most_common_word

#     return result


# print(analyse_text(text))




# Good. Day 2 — OOP and classes.

# word = "car"
# statements = [
#     "car car car red",
#     "car fast",
#     "bike blue",
#     "car car fuel"
# ]

# result = sorted([s for s in statements if word in s.split()],
#                 key= lambda s: s.split().count(word), reverse=True )

# print(result)


numbers = [5, 2, 8, 1, 9, 3]

# Sort normally:
print(sorted(numbers))

# Sort by remainder when divided by 3:
print(sorted(numbers, key=lambda x: x % 3))

# Sort strings by length:
words = ["python", "ai", "engineer", "data"]
print(sorted(words, key=lambda w: len(w)))