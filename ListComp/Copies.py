import copy, json

original = [[['Brawn', 'Strawman'], [1982, 'WWE', 45], 'Wrestler'], [['John', 'Cena'], [1992, 'WWF', 56], 'Wrestler']]
deeply_copied_version = copy.deepcopy(original)
shallow_copied = original[:]
original[0][0].append('Alive')
original.append([['The', 'Rock'], [1965, 'WWF', 57], 'Wrestler'])

string_json = json.dumps(deeply_copied_version, indent = 2)

print(original)
print(deeply_copied_version)
print(shallow_copied)
print(string_json)

