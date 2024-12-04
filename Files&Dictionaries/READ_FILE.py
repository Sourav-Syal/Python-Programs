check_alpha = input("Input the character/letter for which you want to check number of words start from that letter:")
num_words, wrds_s, accum = 0, 0, 0
third_word = []
word_list = []
with open("school_prompt.txt", "r") as ref:
    for line in ref.readlines():
        accum += 1
        temp_lst = line.strip().split()
        third_word.append(temp_lst[2])
        num_words += len(temp_lst)
        for i in range(len(temp_lst)):
            print(temp_lst[i])
            temp_str = temp_lst[i]
            if check_alpha == temp_str[0].lower():
                if temp_str not in word_list:
                    word_list.append(temp_str)
                    wrds_s += 1

print(f"TOTAL WORDS: {num_words}")
print(f"TOTAL LINES: {accum}")
print(f"THIRD WORD OF EVERY LINE: {third_word}")
print(f"TOTAL WORDS STARTING FROM {check_alpha}: {str(wrds_s)}")
print(f"LIST OF THOSE WORDS: {word_list}")