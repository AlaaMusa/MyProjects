import random

print("Step right up to play LUCKY DOUBLES!!")

print("One roll of the dice costs $1.00.")

print("If you roll **LUCKY DOUBLES**, you'll win the FACE VALUE of your dice in $$.")

Rolls = int(input("Ready? Enter number of rolls: "))

Dollors = Rolls * -1


for i in range(Rolls):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
        
    print (f"\nDie1 is {die1} and die2 is {die2}.", end = "")
        
    if die1 != die2:
        print ("No luck here")
        
    else:
        Dollors += die1 + die2; 
        print (f"**LUCKY DOUBLES**!! YOU WON ${die1 +die2}!! CONGRATULATIONS!")
    
print (f"\nYour final total is ${Dollors}.", end = "")

if Dollors < 0:
    print(" House always wins.")
elif Dollors > 0:
    print(" You came out ahead!")
else:
    print(" You broke even.")

