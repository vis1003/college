name = input("Enter file name:")
n = int(input("Enter number of lines to display:"))
with open(name, 'r') as f:
    for i in range(0,n):
        print(f.readline())

word = input("Enter word:")
file = open(name, 'r')
data = file.read()
n = data.count(word)
print("Number of occurrences:", n)

