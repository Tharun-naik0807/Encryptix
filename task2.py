def display_contacts(names, ph_numbers):
    print("\nName\t\t\tPh Number\n")
    for i in range(len(names)):
        print("{}\t\t\t{}".format(names[i], ph_numbers[i]))

def main():
    names = []
    ph_numbers = []
    num = int(input("no of contacts? "))

    for i in range(num):
        name = input("Name: ")
        ph_number = input("Ph Number: ")
        names.append(name)
        ph_numbers.append(ph_number)

    while True:
        print("\n1. Display Contacts")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("0. Exit")
        
        choice = input("Enter  no of your choice: ")

        if choice == '1':
            display_contacts(names, ph_numbers)
        
        elif choice == '2':
            search_term = input("\nEnter search term: ")
            if search_term in names:
                index = names.index(search_term)
                phone_number = ph_numbers[index]
                print("Name: {}, Ph Number: {}".format(search_term, ph_number))
            else:
                print("no name found")
        
        elif choice == '3':
            search_term = input("\nEnter the name of the contact to be update: ")
            if search_term in names:
                index = names.index(search_term)
                new_name = input("Enter new name (or press Enter to keep current): ")
                new_ph_number = input("Enter new ph number (or press Enter to keep current): ")
                if new_name:
                    names[index] = new_name
                if new_ph_number:
                    ph_numbers[index] = new_ph_number
                print("Contact updated.")
            else:
                print("no name found")
        
        elif choice == '4':
            search_term = input("\nEnter the name of the contact to be delete: ")
            if search_term in names:
                index = names.index(search_term)
                names.pop(index)
                ph_numbers.pop(index)
                print("Contact deleted.")
            else:
                print("no name found")
        
        elif choice == '0':
            print("TASK ENDED")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
