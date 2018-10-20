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

