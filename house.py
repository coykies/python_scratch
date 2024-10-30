#Where is live persons from Harry Potter

#what is name person 
name = input("What's your name? ")

match name: 
    #or harry or ron
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
