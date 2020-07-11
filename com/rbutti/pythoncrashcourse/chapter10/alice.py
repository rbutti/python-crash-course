try:
    with open("alice.txt") as f:
        print(f.read())
except FileNotFoundError:
    # print("not found")
    pass
