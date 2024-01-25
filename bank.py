import story

# Accessing the content dictionary
bank = story.content['bank']

def bank_scene():
    print(bank['description'] + " \n")
    print(bank['dialogue'] + "\n")
   
    option = input("A) Engage in a gunfight\nB) Try to resolve peacefully\n").upper()
    if option == "A":
        gunfight()
    elif option == "B":
        resolve_peacefully()
    else:
        print("Invalid option. Please choose again.")
        bank_scene()  

def gunfight():
    print("gun fight")

def resolve_peacefully():
    print("Peace Bro Peace")