num = int(input("enter input number:--"))


def fibo(n):
    a = 0
    b = 1

    if n > 1:
        print("entered valid number")
        print(a)
        print(b)
    else:
        print("entered invalid number")

    for i in range(0, n):
        c = a + b
        a = b
        b = c
        if c <= 100:
            print(c)

fibo(num)