def is_prime(number):
    j = 0
    for i in range(1, number + 1, 1):
        if number % i == 0:
            j = j + 1

    if j == 2:
        return True
    else:
        return False


array = [None] * 20
len = 0
i = 1
while len < 20:
    i = i + 1
    if is_prime(i):
        array[len] = i
        len = len + 1
print(array)
