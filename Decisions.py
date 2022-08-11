import random

randNum = random.randint(1,4)

Name = input("Enter preformer's name: ")

height = int(input(f"Enter {Name}'s height in inches: "))

if height >= 74:
    print(f"{Name} will be playing the role of Giant.")
    
elif height >= 68 and height <=73:
    print(f"{Name} will be playing the role of Hogwarts teacher.")
    
elif height >=58 and height <=67:
    if randNum == 1:
        print(f"{Name} will be playing the role of Hogwarts student in the house of Gryffindor.")
    
    elif randNum == 2:
        print(f"{Name} will be playing the role of Hogwarts student in the house of Slytherin.")
        
    elif randNum == 3:
        print(f"{Name} will be playing the role of Hogwarts student in the house of Ravenclaw.")
    
    else: 
        print(f"{Name} will be playing the role of Hogwarts student in the house of Hufflepuff.")
        
else: 
    print(f"{Name} will be playing the role of House elf.")

    
    
