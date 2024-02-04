arr = [1,45,78,345,678,3465,87,45]

def method1(arr):
    max = arr[0]

    for i in arr:

        if i > max:
            max = i
        
    return max

