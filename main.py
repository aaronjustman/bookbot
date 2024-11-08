book = open("books/frankenstein.txt", "r")
# print(book.read())

character_dict = {}
totalWords = 0

for line in book:
    words = line.split(" ")
    lowered = line.lower()
    totalWords += len(words)
    for c in lowered:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1

# print("character dict:", character_dict)

print("--- Begin report of books/frankenstein.txt ---")
print("total words:", totalWords, "\n")

for key in character_dict:
    print(f"The '{key}' character was found {character_dict[key]} times")

print("--- End report ---")

book.close()
