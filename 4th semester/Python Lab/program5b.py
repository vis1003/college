import re

phno_pattern = re.compile(r'\+\d{12}$')
email_pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
email = []
phno = []
with open('file.txt','r') as f:
    for line in f:
        email.extend(email_pattern.findall(line))
        phno.extend(phno_pattern.findall(line))

print("Email IDs:")
for x in email:
    print(x) 
print("Phone Numbers:")
for x in phno:
    print(x) 
