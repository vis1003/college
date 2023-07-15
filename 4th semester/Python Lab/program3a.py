s = input("Enter a sentence:")
list = s.split()
words = len(list)
digit = 0
upper = 0
lower = 0
for ch in s:
    if ch.isdigit():
        digit = digit + 1
    if ch.isupper():
        upper = upper + 1
    if ch.islower():
        lower = lower + 1
print("Number of words:", words)
print("Number of digits:", digit)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
