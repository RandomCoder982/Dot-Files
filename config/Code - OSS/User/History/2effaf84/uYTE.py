def perfect(num):
    divisbles = []

    for i in range(1, num):
        if num/i == num//i:
            divisbles.append(i)

    return sum(divisbles) == num

perfect_num = []
for i in range(1, 8129):
    if perfect(i):
        perfect_num.append(i)
print(perfect_num)