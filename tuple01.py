def remove_duplicates(lst):
    seen = set()
    new_lst = []
    for tup in lst:
        if tup[0] not in seen:
            seen.add(tup[0])
            new_lst.append(tup)
    return new_lst
lst = [(12.121, 'Tuple1'), (12.121, 'Tuple2'), (12.121, 'Tuple3'), (923232.2323, 'Tuple4')]
result = remove_duplicates(lst)
print(result)