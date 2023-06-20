n = input("Enter a number")
try:
    rev = n[::-1]
    if n == rev:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
except:
    print("Not an integer")

freq = {}
for i in n:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print(freq)
