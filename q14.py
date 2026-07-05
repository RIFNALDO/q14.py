a = float(input("Enter the length of one side, a:"))
b = float(input("Enter the length of one side, b:"))
c = float(input("Enter the length of one side, c:"))

if (a + b + c) and  (a + c > b) and (b + c > a):
    print("Valid Trianlge")
else:
    print("Invalid triangle")