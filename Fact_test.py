x= int (input("Enter the number ="))

def fact(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    return f

result = fact(x)
print(result)
