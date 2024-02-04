arr = [1,45,78,345,678,3465,87,45]

# Finding Maximum Element From Array 


# Method 1 : By Iterating Over Whole Array And Check Every Element
def method1(arr):
    max = arr[0]

    for i in arr:

        if i > max:
            max = i
        
    return max

# Method 2 : By Using Built In Function 'max()'
def method2(arr):

    return max(arr)

# Method 3 : By Sorting Array
def method3(arr):

    arr.sort()
    return arr[len(arr)-1]
