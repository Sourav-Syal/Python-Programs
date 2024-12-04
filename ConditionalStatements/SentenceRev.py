p_phrase = input("Please input the sentence that you would like to check:")
r_phrase = ''
for char in p_phrase:
    r_phrase = char + r_phrase

if p_phrase == r_phrase:
    print("string is reversible")

else:
    print("string is not reversible")