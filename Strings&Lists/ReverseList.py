old_lst = [1,2,3,4,5,6]

new_lst = []
str1 = ""
for i in range(len(old_lst)-1,-1,-1):
    str1 = str1 + " " + str(old_lst[i])

new_lst = str1.split()
print(new_lst)
