Celsius = []
for _ in range(7):
    Celsius.append(int(input("Enter Temp in Celsius for the each day of last week:")))

print("Temp on Sunday: ", Celsius[0])
print("Temp on Monday: ", Celsius[1])
print("Temp on Tuesday: ", Celsius[2])
print("Temp on Wednesday: ", Celsius[3])
print("Temp on Thursday: ", Celsius[4])
print("Temp on Friday: ", Celsius[5])
print("Temp on Saturday: ", Celsius[6])

counter = int(input("For how many days from start of the week you want the average temp?"))
print("Here's the list of temperature recordings for required days: ", Celsius[:counter])

adding = 0
for i in range(counter):
    adding = adding + Celsius[i]

print("Average temperature for the last week: ", adding / counter )
