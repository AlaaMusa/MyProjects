pics = ["\U0001F96F", "\U0001F95E", "\U0001F9C7", "\U0001F354", "\U0001F35F", "\U0001F355", "\U0001F32D", "\U0001F32F", "\U0001F963", "\U0001F957", "\U0001F363"]

food = ["Bagel", "Pancakes", "Waffle", "Hamburger", "Fries", "Pizza", "Hotdog", "Burrito", "Large Soup", "Salad", "Sushi"]

prices = [1, 8, 5, 3, 2, 2, 3, 8, 4, 10, 9]



def printItems(pics, desc, prices):
    
    print("\n\nOne Stop Foods - Menu\n")
    
    print(f" Food Item                     Price")
    print("----------------------------------------")
    
    for i in range(len(food)):
        print (format(f"{pics[i]:<5}{food[i]:<20}{prices[i]:>10}"))   

def printSpecialOffers(desc, prices):

    print("\n***********SPECIAL OFFERS***********")
    
    maxP = max(prices)
    maxPIndex = prices.index(maxP)

    print (f"\nGet our perfect hand crafted {food[maxPIndex]} at ${prices[maxPIndex]}")

    minP = min(prices)
    minPIndex = prices.index(minP)

    print (f"\nOr if your on a budget try the {food[minPIndex]} only at ${prices[minPIndex]}!!")
        
    
def main():
    
    printItems (pics, food, prices)
    
    printSpecialOffers (food, prices)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
        


