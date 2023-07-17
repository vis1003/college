# remove duplicate words and sort the remaining words in alphanumeric order
s = input("Enter a sentence:")
l1 = s.split()
l2 = []
for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
l2.sort()
for i in l2:
    print(i, end=" ")
