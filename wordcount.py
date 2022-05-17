"""Count words in file."""
import sys

# def count_words(file):
#     open_file = open(file)
#     all_words = {}

#     for line in open_file:
#         line = line.rstrip()
#         words = line.split()
#         for word in words:
#             all_words[word] = all_words.get(word, 0) + 1
        
#     return all_words


# # put your code here.

# print(count_words("test.txt"))
# print(count_words("twain.txt"))

def tokenize(filename):
    open_file = open(filename)
    all_words = []

    for line in open_file:
        line = line.rstrip()
        words = line.split()
        all_words.extend(words)
    
    return all_words
            
print(tokenize("test.txt"))            

def count_words(words):
    wordcount = {}

    for word in words: 
        if word not in wordcount:
            wordcount[word] = 1
        else: wordcount[word] += 1
    
    return wordcount

print(count_words(["apple", "berry", "berry", "berry", "cherry", "apple", "cherry", "cherry"]))

def print_word_counts(word_counts):
    for word, count in word_counts.items():
        print(f"{word} {count}")

print(print_word_counts({'apple': 2, 'berry': 3, 'cherry': 3}))


def normalize_text(text):
    open_file = open(file)
    all_words = {}

    for line in open_file:
        line = line.rstrip()
        words = line.split()
        for word in words:
            all_words[word] = all_words.get(word, 0) + 1
        
    return all_words





