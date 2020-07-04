alien_0 = {'color':'green', 'points':5, 'speed': 'medium'}
print(alien_0['color'])

alien_0['x'] = 5
alien_0['y'] = 25
print(alien_0)

jump = 0;
if alien_0['speed'] == 'medium':
    jump = 1

alien_0['x'] = alien_0['x'] +jump

print(alien_0)

del alien_0['speed']
print(alien_0)

print(alien_0.get('speed','Removed'))

print("-------------------------")

aliens = []

for count in range(1,31):
    aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})

print(f"alien cound : {len(aliens)}")