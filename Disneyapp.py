
playAgain = ""
while playAgain == "":
    


    print (f"\nWelcome to the Disneyland app! What would you like to do?\n")
    print (f"1) Enter a new ride",end ="\n")
    print (f"2) View all rides and wait times)",end ="\n")
    print (f"3) View ride stats",end ="\n")
    print (f"4) Quit",end ="\n")
    
    
    rides = ["Pirates of the Caribbean",
    "The Haunted Mansion",
    "Space Mountain",
    "Big Thunder Mountain Railroad",
    "Peter Pan's Flight",
    "Matterhorn Bobsleds",
    "Indiana Jones Adventure",
    "Autopia",
    "Star Wars: Rise of the Resistance",
    "Submarine Voyage"]
    
    waitTimes = [15, 13, 60, 45, 45, 50, 50, 20, 40, 25]
    
    def addNew(r, w):
        newRide = input("\nEnter ride: ")
        newWait = input (f"Enter wait time in minutes for {newRide}: ")
        
        rides.append(newRide)
        waitTimes.append(newWait)
        
        print ("\nData saved.")
    
    
    def viewAll(r, w):
        print ("\nRIDE                          WAIT TIME(MIN)",end="\n")
        print("---------------------------------------------",end="\n")
        for i in range(len(rides)):
            print ("{:35}{}".format(r[i], w[i]))
    
    def viewStats(r, w):
        
        maxW = max(waitTimes)
        maxWIndex = waitTimes.index(maxW)
        
        print (f"Maximum wait time: {rides[maxWIndex]} ({waitTimes[maxWIndex]})")
        
        minW = min(waitTimes)
        minWIndex = waitTimes.index(minW)
        print (f"Minimum wait time: {rides[minWIndex]} ({waitTimes[minWIndex]})")
        
    def main ():
        
        userChoice = input("Enter your choice (1-4): ")
        
        if (userChoice == "1"): 
                    
                addNew(rides, waitTimes)
                
        elif (userChoice == "2"):
                    
                viewAll (rides, waitTimes)
                
        elif (userChoice == "3"):
                    
                viewStats(rides, waitTimes)
                
        else:
                    
            print ("Thank you for using the Disneyland app")
        
        if userChoice < "1" or userChoice > "4":
            print ("\nInvalid Input")
            
        
        
    if __name__ == "__main__":
        main()
    
    playAgain = input("\nPress ENTER to continue...")
    
    







