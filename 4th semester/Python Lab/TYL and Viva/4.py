# reverse and print words in a sentence
s = input("Enter a sentence:")
list = s.split()
rev=[]
for i in list:
    a=i[::-1]
    rev.append(a)
for i in rev:
    print(i,end=" ")