print ("Welcome to Disneyland!")

MaxG = 8
runningTotal = 0
Gcounter = 0

numG = int(input("How many guests in your party? (Maximum 8 guests per party): "))
    

while numG > MaxG or numG < 1 :
    
    numG = int(input("Number of guests must be between 1 and 8. Please re-enter: "))
    continue

for i in range(numG):
    Gcounter += 1
    ageG = int(input(f"\nEnter age of guest {Gcounter}: "))
    
    if ageG >= 0 and ageG <= 2:
        price = 0
        runningTotal += price
        print (f"Ticket cost for guest {Gcounter} ({ageG} years): $0.00")
        print (f"      Total cost for party: ${runningTotal:.2f}")
        
    
    elif ageG >= 3 and ageG <= 9:
        
        price = 125
        runningTotal += price
        print (f"Ticket cost for guest {Gcounter} ({ageG} years): $125.00")
        print (f"      Total cost for party: ${runningTotal:.2f}")
    
    else:
        
        price = 155
        runningTotal += price
        print (f"Ticket cost for guest {Gcounter} ({ageG} years): $155.00")
        print (f"      Total cost for party: ${runningTotal:.2f}")
        
Genie = input(f"\nWould you like to add the benefits of Genie+ for just $20.00 per ticket? (y/n): ")

while Genie.lower() != "y" and Genie.lower() != "n":
    Genie = input("\nInput must be y or n. Would you like to add the benefits of Genie+ for just $20.00 per ticket? (y/n):  ")

if Genie.lower() == 'y':
    Gcost = numG * 20
    print ("\nYOUR RECEIPT")
    print ("--------------------------------------")
    print (f"Ticket costs ({numG} guests): ${runningTotal:.2f}")
    print (f"Genie+ surcharge: ${Gcost:.2f}")
    print ("--------------------------------------")
    
else:
    Gcost = 0
    print ("\nYOUR RECEIPT")
    print ("--------------------------------------")
    print (f"Ticket costs ({numG} guests): ${runningTotal:.2f}")
    print ("Genie+ surcharge: $0.00")
    print ("--------------------------------------")
    
while Genie.lower() != "y" and Genie.lower() != "n":
    Genie = input("Input must be y or n. Would you like to add the benefits of Genie+ for just $20.00 per ticket? (y/n):  ")
    
print (f"TOTAL COSTS: ${runningTotal + Gcost:.2f}")
print ("\nEnjoy your stay at Disneyland, the happiest place on earth!")
        

