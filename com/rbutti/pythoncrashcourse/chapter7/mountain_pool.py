responses = {}

poll_active = True

while poll_active:
    name = input("name :")
    bike = input("bike :")

    responses[name] = bike
    repeat = input("repeaat : ")
    if repeat == "no":
        poll_active = False

print(responses)