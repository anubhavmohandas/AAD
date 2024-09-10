def compare_chefs(a, b):
    chef1 = 0
    chef2 = 0
    
    for i in range(3):
        if a[i] > b[i]:
            chef1 += 1 #chef1 gains 1 point
        elif a[i] < b[i]:
            chef2 += 1 #chef2 gains 1 point
        elif a[i] == b[i]:
            chef1 += 0 #chef1 gains 0 point
            chef2 += 0 #chef2 gains 0 point
    
    return [chef1, chef2]

# Provided Input
a = [27, 48, 70]
b = [89, 26, 7]

output = compare_chefs(a, b)
print(output)