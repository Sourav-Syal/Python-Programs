def one_letter_feedback(guessed_let, correct_let, correct_word):
    if guessed_let == correct_let:
        return 'Y'
    elif guessed_let in correct_word:
        return 'y'
    else:
        return '-'

def give_feedback(guess, correct_word):
    return [one_letter_feedback(guessed_let, correct_let, correct_word)
        for (guessed_let, correct_let) in zip(guess, correct_word)]

print(give_feedback('hello', 'hails'))