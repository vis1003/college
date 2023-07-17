# check and print strings starting with "hello" and ending with a number
s = []
n = int(input("Enter number of strings:"))
print("Enter", n, "strings:")
for i in range(0, n):
    a = input()
    s.append(a)
new=[]

for i in s:
    if i.startswith("Hello"):
        if i[-1].isdigit():
            new.append(i)

print("New list:")
for i in new:
    print(i)