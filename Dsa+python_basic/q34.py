sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique Words:", " ".join(unique_words))