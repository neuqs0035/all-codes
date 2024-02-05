arr = [1,34,456,657,68,3,76,57]

max1 = arr[0]
max2 = arr[1]

for i in arr:

    if i >= max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i
        
print(max1,max2)

