import re


def isphonenumber(test):
    if len(test) != 12:
        return False
    else:
        for i in range(3):
            if not test[i].isdigit():
                return False
        if test[3] != '-':
            return False
        for i in range(4, 7):
            if not test[i].isdigit():
                return False
        if test[7] != '-':
            return False
        for i in range(8, 12):
            if not test[i].isdigit():
                return False
        return True


def isphonenumber_re(test):
    if re.match(r"^\d{3}-\d{3}-\d{4}$", test):
        return True
    else:
        return False


string = input("Enter your string:")
print("Without using regular expression:")
for i in range(len(string)):
    s = string[i:i + 12]
    pattern = isphonenumber(s)
    if pattern:
        print(s)

print("Using regular expression:")
for i in range(len(string)):
    s = string[i:i + 12]
    pattern = isphonenumber_re(s)
    if pattern:
        print(s)
