def height_conv(list_height, converter):
    res_list = []
    if converter == 'Inches' or converter == 'inches':
        for dictionary in list_height:
            res_list.append(f"{(dictionary['Feet'] * 12) + dictionary['Inches']} Inches")

    elif converter == 'Centimeters' or converter == 'centimeters':
        for dictionary in list_height:
            res_list.append(f"{((dictionary['Feet'] * 12) + dictionary['Inches']) * 2.54} Centimeters")

    elif converter == 'Meters' or converter == 'meters':
        for dictionary in list_height:
            res_list.append(f"{((dictionary['Feet'] * 12) + dictionary['Inches']) * 0.0254} Meters")

    return res_list

list_of_input, dict_height = [], {}

signal = 'N'
while signal != 'Y':
    dict_height['Feet'] = int(input("Enter Feets:"))
    dict_height['Inches'] = int(input("Enter Inches:"))
    list_of_input.append(dict(dict_height))
    signal = input("Would you like to stop(Y/N)?")

conv = input("Enter in which Unit you want to convert the height(Inches/Centimeters/Meters):")

result_set = height_conv(list_of_input, conv)

idx = 0
for height in result_set:
    print(f"{list_of_input[idx]['Feet']} Feet {list_of_input[idx]['Inches']} Inches is equal to {height}")
    idx += 1

