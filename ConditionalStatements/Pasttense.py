words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []
for word in words:
    if word[-1] == 'e':
        word = word + 'd'
        past_tense.append(word)

    else:
        word = word + 'ed'
        past_tense.append(word)

print(past_tense)