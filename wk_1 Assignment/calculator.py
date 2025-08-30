a =float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("choose an operation(+,-,*,/): ")


if op =="+":
    print(f"{a} +{b} ={a+b}")
elif op == "-":
    print(f"{a} -{b} = {a-b}")
elif op== "*":
    print(f"{a} *{b} ={a*b}")
elif op =="/":
    print(f"{a} /{b} = {a/b}" if b !=0 else "Error: Cannot divide by zero.")
else:
    print("Invalid operation.")

