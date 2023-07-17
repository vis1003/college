# remove duplicate words of length greater than 10
s = input("Enter a sentence:")
list = s.split()
new=[]
for i in list:
    if len(i)>=10:
        if i in new:
            continue
        else:
            new.append(i)
    else:
        new.append(i)

for i in new:
    print(i,end=" ")