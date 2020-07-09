def greet_user(user, msg="rocks"):
    print(f"hello world{user.title()} {msg.title()}")


greet_user("ravi", "rocks")
greet_user("john")
greet_user(msg="sparrow", user="jack")