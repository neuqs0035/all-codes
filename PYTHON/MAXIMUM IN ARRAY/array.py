arr = [1,45,78,345,678,3465,87,45]

# Finding Maximum Element From Array 


# Method 1 : By Iterating Over Whole Array And Check Every Element
def method1(arr):
    max = arr[0]

    for i in arr:

        if i > max:
            max = i
        
    return max

