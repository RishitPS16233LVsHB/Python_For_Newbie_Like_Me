def display_friends(friends_dict):
    print("Name\t\tPhone Number")
    for name, phone_number in friends_dict.items():
        print(f"{name}\t\t{phone_number}")

def add_friend(friends_dict, name, phone_number):
    friends_dict[name] = phone_number
    return friends_dict

def delete_friend(friends_dict, name):
    if name in friends_dict:
        del friends_dict[name]
    else:
        print("Friend not found")

def modify_phone_number(friends_dict, name, new_phone_number):
    if name in friends_dict:
        friends_dict[name] = new_phone_number
    else:
        print("Friend not found")

def check_friend_presence(friends_dict, name):
    return name in friends_dict

def display_sorted_friends(friends_dict):
    sorted_friends = sorted(friends_dict.items())
    print("Name\t\tPhone Number")
    for name, phone_number in sorted_friends:
        print(f"{name}\t\t{phone_number}")

friends = {}
while True:
    print("\n1. Display all friends")
    print("2. Add a new friend")
    print("3. Delete a friend")
    print("4. Modify phone number of a friend")
    print("5. Check if a friend is present")
    print("6. Display friends in sorted order")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_friends(friends)
    elif choice == '2':
        name = input("Enter friend's name: ")
        phone_number = input("Enter friend's phone number: ")
        friends = add_friend(friends, name, phone_number)
    elif choice == '3':
        name = input("Enter friend's name to delete: ")
        delete_friend(friends, name)
    elif choice == '4':
        name = input("Enter friend's name to modify phone number: ")
        if name in friends:
            new_phone_number = input("Enter new phone number: ")
            modify_phone_number(friends, name, new_phone_number)
        else:
            print("Friend not found")
    elif choice == '5':
        name = input("Enter friend's name to check: ")
        if check_friend_presence(friends, name):
            print(f"{name} is present in the list of friends")
        else:
            print(f"{name} is not present in the list of friends")
    elif choice == '6':
        display_sorted_friends(friends)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
