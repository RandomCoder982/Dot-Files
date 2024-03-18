for i in range(10):
   for j in range(i):
    if i != 0 and j != 0:
        if i/j == i//j:
            print(f"i={i}, j={j}, {i/j}")

def perfect(num):
    divisbles == []

    for i in range(1, num):
        if num/i == num//i:
            divisbles.append(i)


