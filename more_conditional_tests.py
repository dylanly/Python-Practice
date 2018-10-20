name = "Dylan Ly"
print("Are there 7 characters in name? I predict True.")
print(len(name) == 7)

print("Are there 8 characters in name? I predict False.")
print(len(name) == 8)

print("Is the username Dylan Ly taken? I predict True")
print(name.lower() == name.lower())

print("Is the username dylan ly taken? I predict False.")
print(name.lower() == name.lower())

if (name.lower() == "dylan ly"):
    print("Ayy nigga")
else:
    print("oh what the fuc")
    
print("\n")


number = 6
if number == 6:
    print("YOU GOT IT MFER")
if number < 6:
    print("Too low!")
if number > 6:
    print("Too high!")

print("\n")

my_age = 19
vincent_age = 22

if my_age > 18 and vincent_age > 18:
    print("True")
if my_age > 18 and vincent_age < 18:
    print("False")
    
print("\n")

if my_age > 21 or vincent_age > 21:
    print("True")
if my_age < 21 or vincent_age < 21:
    print("False")
else:
    print("neither")
    
print("\n")
    
list_friends = ['Ken', 'Mikey', 'Mitchell', 'Micow']
print("Below you can see all my best friends!\n")
for friend in list_friends:
    print(friend)
if 'Drew' not in list_friends:
    print("\n:O \nDrew is not in my friends list!!\n")
    list_friends.append('Drew')
    for friend in list_friends:
        print(friend)
    print("\nI fixed my best friend's list hehe xD")

