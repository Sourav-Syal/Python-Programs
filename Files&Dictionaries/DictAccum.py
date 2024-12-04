#Defining a function to count all letters
def character_count(file_obj):
    letter_count, lines = {}, 0
    punctuations = [' ', '.', ':', ',', '!', '\n']
    for character in file_obj:
        if character not in punctuations:
            letter_count[character.lower()] = letter_count.get((character.lower()),0) + 1
        elif character == '\n':
            lines += 1
    return letter_count, lines

#Defining a function to count vowels
def count_vowels(dictionary):
    vowels, occurrence = 0, 0
    lst = list(dictionary.keys())
    for c in lst:
        if c in ['a','e','i','o','u']:
            vowels += 1
            occurrence += dictionary[c]
    return vowels, occurrence


#Creating read object to open a file
ref = open("emotion_words.txt", "r")
characters = ref.read()

#Calling functions
letters, line_count = character_count(characters)
vowel, vowel_count = count_vowels(letters)

#Printing Results
if vowel == 5:
    print("ALL VOWELS (a,e,i,o,u) appeared")
else:
    print(f"Only {vowel} of them have appeared")

print(f"Number of lines: {line_count}")
print(f"Occurrence of vowels only: {vowel_count}")
print(f"Occurrence of Words \n{letters}")

ref.close()