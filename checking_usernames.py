current_users = ['kevin', 'dylan', 'vincent', 'gen', 'micow', 'mitchell']
new_users = ['kevin', 'Mikey', 'Ken', 'Dylan', 'Drew']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, that username is taken")
    else:
        print("That username is available!")
    
