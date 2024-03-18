def perfect(num):
    divisbles = []

    for i in range(1, num):
        if num/i == num//i:
            divisbles.append(i)

    return sum(divisbles) == num


print(perfect(7))