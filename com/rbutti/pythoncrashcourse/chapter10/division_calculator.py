try:
    print(5/0)
except ZeroDivisionError:
    print("Error")
else:
    print("Success")