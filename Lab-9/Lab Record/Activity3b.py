dict1 = eval(input("Enter first dictionary (e.g. {'a':1, 'b':2}): "))
dict2 = eval(input("Enter second dictionary (e.g. {'b':3, 'c':4}): "))

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key not in merged_dict:
        merged_dict[key] = value

print("Merged dictionary:", merged_dict)
