arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(arr[1])
arr[1] = 9
print(arr)
print("length = ", len(arr))

for x in arr:
    print(x)

arr.append(10)
print(arr)
arr.pop(4)
print(arr)