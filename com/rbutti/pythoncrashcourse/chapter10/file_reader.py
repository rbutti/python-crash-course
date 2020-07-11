with open('pi_digits.txt') as file_object:
    contects = file_object.read()
print(contects.rstrip())

print('----------')
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

print('----------')
str = ""
for line in lines:
    print(line.rstrip())
    str += line.strip()

print('----------')
print(str)
if "141" in str:
    print("found")