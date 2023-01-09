
comb = []
for a in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:
    for b in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        if a == b:
            comb.append(b)

result = []

for elements in comb:
    if elements not in result: 
        result.append(elements)

print(result)
