def linear_search(arr, target):
    count=0
    for i in range(len(arr)):
        if arr[i] == target:
            count=1
    if count==1:
        print("The searched element",target," is found at position ",i)
    else:
        print("Element not found!")
        

def binary_search(arr, target):
    count=0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            count=1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if count==1:
        print("The searched element",target," is found at position ",mid)
    else:
        print("Element not found!")

arr=[]
n=int(input("Enter the no. of elements to be added  :"))
for i in range(int(n)):
    k=int(input("Enter the elements:  "))
    arr.append(k)

target=int(input("Enter the number to searched"))
print("")
print("")
print("")
print("Select the type of search you want to perform  :")
print("")
print("press l for lenear search")
inpp=input("press b for binary search    ")
print("")
if inpp=='l' or inpp=='L':
    linear_search(arr, target)
elif inpp=='b' or inpp=='B':
    binary_search(arr, target)
else:
    print("Invalid Input")