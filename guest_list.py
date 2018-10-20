guest_list = ['Dylan']

guest_list.append('Micow')
guest_list.append('Ken')
guest_list.append('Mitchell')
guest_list.append('Mikey')

print(guest_list)

message = "Hey, " + guest_list[1] + " I'm having a party this friday, trying to come thruuu?"

print(message)

#Mikey couldn't come up to seattle :(

guest_list.remove('Mikey')
print(guest_list)

guest_list.append('Leo')

message = "Hey, " + guest_list[-1] + " I'm having a party this friday, trying to come thruuu?"
print(message)

good_news = "Hey everyone, I got a bigger table so I can invite more people now!"
print(good_news)

guest_list.insert(0, 'Mommy')
guest_list.insert(10, 'Daddy')
guest_list.insert(3, 'Drew')
print(guest_list)

bad_news = "Sorry guys, this company is whack and a new table won't be here in time for the party and I can only invite 2 people now"
print(bad_news)

popped_guest = guest_list.pop()
print(popped_guest)
print(guest_list)


