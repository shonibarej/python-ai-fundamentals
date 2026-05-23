
# words =["python", "ai", "engineer", "data", "analyst", "uk"]

# def filterby_word_length(word: list[str], min_length:int) -> list[str]:
#     return [ w for w in word if len(w) > min_length]

# print(filterby_word_length(words, 3))



# results = []
# def analyse_text(text: str) -> dict:
#     return [ w]

text = "the cat sat on the mat the cat"


def analyse_text(text: str):
    results = {}
    text_split = text.split()
    word_count = len(text_split)
    results["word_count"] = word_count
    unique_word_count= len(set(text_split))
    results["unique_word_count"] = unique_word_count
    most_common_word = max(text_split, key= text_split.count)
    results["most_common_word"] = most_common_word
    sum_length = sum(len(w) for w in text_split)
    avg_word_length = sum_length / word_count
    results["avg_word_length"] = avg_word_length
    return results

print(analyse_text(text))

    



