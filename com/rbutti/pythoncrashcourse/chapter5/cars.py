cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if(car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

age_0 = 22
age_1 = 21
print((age_0 >= 21 and age_1 >= 21))

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)


jack = []
if jack:
    for j in jack:
        print("hello")
else:
    print("bye")