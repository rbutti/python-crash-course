def build_profile(fname, lname, **user_profile):
    user_profile['fname'] = fname
    user_profile['lname'] = lname
    print(user_profile)

build_profile("ravi","kiran",age=2,location="uk")