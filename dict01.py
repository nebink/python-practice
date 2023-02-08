def assign_index_to_max_value(d):
    result = {}
    for key, values in d.items():
        max_value = max(values)
        max_index = values.index(max_value)
        result[key] = max_index
    return result
d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
print(assign_index_to_max_value(d))

