import os

class Contact:

    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email



def addContact(contact):
    with open("contact.txt", "a") as file:
        file.write("%s | %s | %s\n" % (contact.name, contact.number, contact.email))

def deleteContact(name):
    with open ("contact.txt", "r") as file:
        lines = file.readlines()
        counter = 0
        for line in lines:
            div = line.strip().split(" | ")
            if name == div[0]:
                print(line)
                decision = input("You sure you want to delete this contact? 1 - YES | 2 - NO")
                if  decision not in ("1","2"):
                    print("Please provide an acceptable answer!")
                    return deleteContact(name)
                else:
                    if decision == "1":
                        del lines[counter]
                        with open("contact.txt", "w") as file:
                            file.writelines(lines)
                        print("Contact succesfully removed!")
                        return 0
                    else:
                        print("Action cancelled")
                        return -1
            else:
                counter += 1

        print("Contact not found!")
        return None

def viewContact(name):
    with open ("contact.txt", "r") as file:
        lines = file.readlines()
        counter = 0
        for line in lines:
            div = line.strip().split(" | ")
            if name == div[0]:
                return line
            
    print("Contact not found!")
    return None




