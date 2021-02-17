phrase = input('Enter the phrase you\'d like me to make into an acronym ')

words = phrase.split()

acronym = ''

for word in words:
    acronym += word[0].upper() + "."

print(acronym)
