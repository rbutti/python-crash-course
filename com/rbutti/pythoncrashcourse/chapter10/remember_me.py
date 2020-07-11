import json

def greet_user():
    filename = "user.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except:
        username = input("what is your name")
        with open(filename,'w') as f:
           json.dump(username,f)
    print(f"Hello {username.title()}")

greet_user()