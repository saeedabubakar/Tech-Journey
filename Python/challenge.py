friends = []
number = int(input("how many friends do you want to add "))
for i in range(number):
    name = input("Enter friend's name: ")
    friends.append(name) 
print("your friends")
for friend in friends:
    print(friend)