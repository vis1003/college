roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
r=input("Enter the Roman number:")
j=roman[r[0]]
int=0
for i in r:
    n=roman[i]
    if j<n:
        int=int+n-2*j
    else:
        int=int+n
    j=n

print(int)