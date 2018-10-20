dylan = {'first_name': 'Dylan', 'last_name': 'Ly', 'city': 'Tacoma'}
print(dylan['first_name'])
print(dylan['last_name'])
print(dylan['city'])


print("Dylan was born in " + dylan['city'] + "!")

for k in sorted(dylan.keys()):
    print("\nKey: " + k)

