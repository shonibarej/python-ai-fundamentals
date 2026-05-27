words =["python", "ai", "engineer", "data", "analyst", "uk"]

def filterby_word_length(word: list[str], min_length:int) -> list[str]:
    return [ w for w in word if len(w) > min_length]

print(filterby_word_length(words, 3))



# results = []
# def analyse_text(text: str) -> dict:
#     return [ w]

text = "the cat sat on the mat the cat"


def analyse_text(text: str) -> dict:
    results = {}
    text_split = text.split()
    word_count = len(text_split)
    results["word_count"] = word_count
    unique_word_count= len(set(text_split))
    results["unique_word_count"] = unique_word_count
    most_common_word = max(text_split, key= text_split.count)
    results["most_common_word"] = most_common_word
    sum_length = sum(len(w) for w in text_split)
    print(sum_length)
    avg_word_length = sum_length / word_count
    results["avg_word_length"] = avg_word_length
    return results

print(analyse_text(text))
print(len(text))

    
import json

def load_config(path: str, required_keys: list[str]) -> dict:
    with open("config.json", "r") as f:
        data = json.load(f)
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
    return data
   



# print(load_config("config.json", ["model", "life"] ))


# import time

# def retry(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(3):
#             try:
#                 return func(*args, **kwargs)
#             except Exception:
#                 print ("Failed, retrying...")
#     return wrapper


import random          
    
# @retry
# def flaky_function():
#     if random.random() < 0.7:
#         raise Exception("Failed!")
#     return "Success"

# print(flaky_function())


# def retry(max_attempts=3, delay=1.0):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(max_attempts):
#                 try: 
#                     return func(*args, **kwargs)
#                 except Exception:
#                    print(f"Failed, retrying in {delay}s") 
#                    time.sleep(delay)
#         return wrapper
#     return decorator


# @retry(max_attempts=3, delay=1.0)
# def flaky_function():
#     if random.random() < 0.7:
#         raise Exception("Failed!")
#     return "Success"

# print(flaky_function())

# flaky_function = retry(max_attempts=3, delay=1.0)(flaky_function)

# import  time
# import random
# import functools

# def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             last_exception = None
#             for attempt in range(1, max_attempts + 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as e:
#                     last_exception = e
#                     if attempt == max_attempts:
#                         raise
#                     print(f"Attempt {attempt}/{max_attempts} failed: {e}. Retrying in {delay}")
#                     time.sleep(delay)
#         return wrapper
#     return decorator



# @retry(max_attempts=3, delay=0.5, exceptions=(ValueError,))
# def flaky_function():
#     if random.random() < 0.7:
#         raise ValueError("API unavailable")
#     return "Success"

# print(flaky_function())


# Good. Day 2 — OOP and classes.

# class Dog:
#     def __init__(self, name: str, breed: str):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} says woof!")

#     def describe(self):
#         print(f"{self.name} is a {self.breed}")


# dog1 = Dog("Rex", "Labrador")
# dog2 = Dog("Buddle", "Poodle")

# dog1.bark()
# dog2.bark()
# dog1.describe()
# dog2.describe()



import json
# 1. Write a dict to a JSON file:
config = {
    "model": "gpt-4o",
    "temperature": 0.0,
    "max_tokens": 1000,
    "tags": ["rag", "production", "uk"]
}


with open("config.json", "w") as f:
    json.dump(config, f, indent= 2)

# 2. Read it back:
with open("config.json", "r") as f:
    loaded = json.load(f)
    print(loaded)
    print(type(loaded))

# 3. Convert dict to string (used when sending data over APIs):
json_string = json.dumps(config)
print(json_string)
print(type(json_string))

# 4. Convert string back to dict:
back_to_dict = json.loads(json_string)
print(back_to_dict)
print(type(back_to_dict))

if __name__ == "__main__":
    text = "the cat sat on the mat the cat"
    print(analyse_text(text))
    print(load_config("config.json", ["model", "temperature"]))