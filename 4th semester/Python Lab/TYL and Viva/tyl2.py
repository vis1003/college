a = int(input("Enter lower limit:"))
b = int(input("Enter upper limit:"))

if a <= 2:
    print(2)

for i in range(a, b):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            print(i)
            break
