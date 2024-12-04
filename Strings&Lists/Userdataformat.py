counter = int(input("how many fruits you want to add?"))

str1 = ""
for _ in range(counter):
    userinput = input("Enter name of fruits:")
    str1 = str1 + userinput + " "

print(", ".join(str1.split()))

