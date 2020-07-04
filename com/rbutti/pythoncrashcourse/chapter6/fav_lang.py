favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("-------------------------")

for name in sorted(favorite_languages.keys()):
    print(name.title())

print("-------------------------")

for name in set(favorite_languages.values()):
    print(name.title())

favorite_languages = {
'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }

for name, languages in favorite_languages.items():
    print(name.title())
    for language in languages:
        print(language)