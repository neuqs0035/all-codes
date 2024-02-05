def sumelements(arr):

    sum = 0

    for i in arr:

        sum += i

    return sum

def sumelements2(arr):

    return sum(arr)


arr = [3,35,34,456,5765,756,7678,24,3434,5435]

print("Sum Of Elements = " , sumelements(arr))
print("Sum Of Elements = " , sumelements2(arr))