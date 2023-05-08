def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[3] Option 3")
    print("[4] Option 4")
    print("[5] Exit the program")

menu()
option = int(input("enter your option: "))

while option != 5: 
    if option == 1:
        #do option 1 stuff
        print("option 1 has been selected")
    elif option == 2:
        # do option 2 stuff
        print("option 2 has been selected")
    else:
        print("invalied option. ")

    print()    
    menu()
    option = int(input("enter your option: "))

print("Thank for using this program goodbye")