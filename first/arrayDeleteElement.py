from array import *
arr = array('i', [])

num = int(input("Enter the length of an array "))
for i in range(num):
     n = int(input("Enter the value "))
     arr.append(n)
val = int(input("Enter the value for delete "))
c=0
for ele in arr:
    if ele == val:
        arr.pop(c)
        break
    c+=1
print(arr)