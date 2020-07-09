def get_name(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person


age = 0
while age in range(0, 3):
    print(get_name("ravi", "kiran", age))
    age += 1
