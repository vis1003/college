# check if entered strings are usn and print them
s = []
n = int(input("Enter number of strings:"))
print("Enter", n, "strings:")
for i in range(0, n):
    a = input()
    s.append(a)
usn = []
for str in s:
    if len(str)==10:
        if str[0].isdigit() and str[3].isdigit() and str[4].isdigit() and str[7].isdigit() and str[8].isdigit() and str[9].isdigit():
            if str[1].isalpha() and str[2].isalpha() and str[5].isalpha() and str[6].isalpha():
                usn.append(str)

print(usn)
