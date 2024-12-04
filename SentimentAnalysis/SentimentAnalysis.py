resultingdatafile = open("resulting_data.csv", "w")
twitterdatafile = open("project_twitter_data.csv", "r")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#Function to count number of positive words
def get_pos(str_sentence):
    str_sentence = strip_punctuation(str_sentence)
    temp_lst = str_sentence.split()

    count = 0
    for word in temp_lst:
        if word in positive_words:
            count += 1
    return count

#Function to count number of negative words
def get_neg(str1_sentence):
    str1_sentence = strip_punctuation(str1_sentence)
    temp_lst = str1_sentence.split()

    tot = 0
    for word in temp_lst:
        if word in negative_words:
            tot += 1
    return tot

#Function to eliminate punctuations from tweet
def strip_punctuation(str_val):
    for i in punctuation_chars:
        str_val = str_val.replace(i,"")
    return str_val

#Function to write result sets in the file
def writedatafile(resultingdatafile):
    resultingdatafile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingdatafile.write("\n")

    lines = twitterdatafile.readlines()
    NotUsed = lines.pop(0)
    for line in lines:
        rows = line.strip().split(',')
        resultingdatafile.write("{}, {}, {}, {}, {}".format(rows[1], rows[2], get_pos(rows[0]), get_neg(rows[0]),
                                                            (get_pos(rows[0]) - get_neg(rows[0]))))
        resultingdatafile.write("\n")

#Calling function with the writing object
writedatafile(resultingdatafile)

#Closing the file...
twitterdatafile.close()
resultingdatafile.close()