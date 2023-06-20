def fibonacci(n):
    t1 = 0
    t2 = 1
    print(t1, t2, end=" ")
    for i in range(0, n):
        t3 = t1 + t2
        print(t3, end=" ")
        t1 = t2
        t2 = t3


try:
    n = int(input("Enter a number:"))
    fibonacci(n)

except:
    print("Enter an integer number")
