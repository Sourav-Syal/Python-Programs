def divisibility(num_list, integer):
    remainder_list = list(map(lambda x: (x,x % integer), num_list))
    ret_list = []

    for t in sorted(remainder_list):
        if t[1] == 0:
            print(f"Number {t[0]} is completely divisible by {integer}\n")
        else:
            ret_list.append((f"Num: {t[0]}", f"Remainder: {t[1]}"))

    return ret_list

#taking user input
user_input, list_input = 1, []
while user_input != 0:
    user_input = int(input("Enter list of integers that you want to check the divisibility(Enter 0 once you're done):"))
    if user_input != 0:
        list_input.append(user_input)

factor = int(input("Enter the number with whom you want to check the divisibility:"))
res_list = divisibility(list_input, factor)

print(f"HERE IS THE LIST OF OTHER NUMBERS WHO'RE LEFT WITH REMAINDERS \n{res_list}")
