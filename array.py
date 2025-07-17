arr = [1,2,3,4]
x = len(arr)
print(arr[x-1])
print(arr[len(arr)-1])

arr.clear()

for i in range(len(arr)):
    arr.pop()


if len(arr) == 0:
    print("List is empty")
else:
    print("List is not empty")

