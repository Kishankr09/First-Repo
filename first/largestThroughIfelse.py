n1 = int(input("Enter 1st number "))
n2 = int(input("Enter 2nd number "))
n3 = int(input("Enter 3rd number "))
if(n1>n2):
    if(n1>n3):
        print("largest", n1)
    else:
         print("largest", n3)
else:
    if (n2 > n3):
        print("largest", n2)
    else:
        print("largest", n3)