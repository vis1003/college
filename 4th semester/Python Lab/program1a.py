test1 = int(input("Enter test 1 marks:"))
test2 = int(input("Enter test 2 marks:"))
test3 = int(input("Enter test 3 marks:"))
total = test1 + test2 + test3
avg = (total - min(test1, test2, test3)) / 2
print("Average=",avg)
