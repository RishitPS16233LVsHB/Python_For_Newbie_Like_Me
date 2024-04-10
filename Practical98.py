def update_phonebook(phonebook):
    while True:
        print("Phonebook:", phonebook)
        choice = input("Enter 'check' to check a name, 'update' to update phone number, or 'quit' to exit: ")
        if choice == 'quit':
            break
        elif choice == 'check':
            name = input("Enter the name to check: ")
            if name in phonebook:
                print("Phone number for", name, "is", phonebook[name])
            else:
                print("Name not found in the phonebook.")
        elif choice == 'update':
            name = input("Enter the name to update: ")
            number = input("Enter the new phone number: ")
            phonebook[name] = number
            print("Phone number updated successfully.")
        else:
            print("Invalid choice. Please try again.")

# Example usage:
phonebook = {'Alice': '1234567890', 'Bob': '9876543210'}
update_phonebook(phonebook)
