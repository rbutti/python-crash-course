bicycles = ['trek','redline']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])

print(f"message {bicycles[0]}")

bicycles.append('blueline')
print(bicycles)


del bicycles[0]
print(bicycles)

bicycles.append('drax')
print(bicycles)


popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

bicycles.insert(0,"yellowline")
print(bicycles)

bicycles.remove('blueline')
print(bicycles)

