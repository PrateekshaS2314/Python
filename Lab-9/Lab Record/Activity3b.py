def merge_dict(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

print("Enter first dictionary (format: key1:value1, key2:value2):")
dict1_input = input()

print("Enter second dictionary (format: key1:value1, key2:value2):")
dict2_input = input()

dict1 = {key: value for key, value in (item.split(":") for item in dict1_input.split(","))}
dict2 = {key: value for key, value in (item.split(":") for item in dict2_input.split(","))}

result = merge_dict(dict1, dict2)

print("Merged dictionary:", result)
