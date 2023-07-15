import difflib

s1 = input("Enter 1st sentence:")
s2 = input("Enter 2nd sentence:")
result = difflib.SequenceMatcher(a=s1.lower(), b=s2.lower())
print(result.ratio())