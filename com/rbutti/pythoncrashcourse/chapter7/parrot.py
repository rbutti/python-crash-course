message = input("type something:")
print(message)

age = input("How old are your:")
age = int(age)
if age > 10:
    print("you can vote")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message =  input(prompt)
    if message == 'quit':
        active = False
        break
    else:
        print(message)
