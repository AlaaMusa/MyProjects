import math

class Ticket:
    __ticketType: str
    __baseCost: int
    __discountAmount: float
    __geniePlusCharges: float
    __totalTicketCost: float
    
    def __init__(self, ttype, bct):
        
        self.__ticketType  = ttype
        self.__baseCost = bct
        self.calc_discount()
        self.calc_genie_plus_charges()
        self.calc_total_ticket_cost()
    
    def calc_discount(self):
        yesNo = input(f"Is guest under ten years old or a veteran of the U.S. Armed Forces?: " )
        if (yesNo == 'y'):
            self.__discountAmount = self.__baseCost * .15
        else:
            self.__discountAmount = 0
            
    def calc_genie_plus_charges(self):
        yesNo = input(f"Would you like to add Genie Plus to your ticket for $20.00?: ")
        if(yesNo == 'y'):
            self.__geniePlusCharges = 20
        else: 
            self.__geniePlusCharges = 0
    
    def calc_total_ticket_cost(self):
        self.__totalTicketCost = self.__baseCost - self.__discountAmount + self.__geniePlusCharges
        
    def print_ticket(self):
        print(f"{self.__ticketType:<30}{self.__baseCost:>10.2f}{-self.__discountAmount:>10.2f} {self.__geniePlusCharges:>10.2f}{self.__totalTicketCost:>15.2f}")
    
    @property     
    def ticketType(self):
        return self.__ticketType
        
    @property     
    def baseCost(self):
        return self.__baseCost
        
    @property     
    def discountAmount(self):
        return self.__discountAmount
        
    @property     
    def geniePlusCharges(self):
        return self.__geniePlusCharges
    
    @property     
    def totalTicketCost(self):
        return self.__totalTicketCost
        


tickets = []

def main():
    
    another = "y"
    
    while another.lower() == "y":
        print ("\n\nWelcome to Disneyland!")
        print("Please select your ticket type:")
        print("1) 1-Day Single Park Ticket: $125.00")
        print("2) 1-Day Park Hopper Ticket: $185.00")
        print("3) 2-Day Single Park per Day Ticket: $225.00")
        print("4) 2-Day Park Hopper Ticket: $260.00")
        
        selection = int(input("\nYour selection =======> "))
        
        if selection == 1:
            ttype = "1-Day Single Park Ticket"
            bct = 125.00
        elif selection == 2:
            ttype = "1-Day Park Hopper Ticket"
            bct = 185.00
        elif selection == 3:
            ttype = "2-Day Single Park per Day Ticket"
            bct = 225.00
        elif selection == 4:
            ttype = "2-Day Park Hopper Ticket"
            bct = 260.00
        
        
        
        tickets.append(Ticket(ttype, bct))
        
        another = input("\nAdd another ticket to your order? (y/n): ")
    
    print("\n\nYOUR ORDER:\n")
    print("{:<20}{:>20}{:>13}{:>12}{:>15}".format("TICKET TYPE", "BASE COST", "DISCOUNT", "GENIE+", "TOTAL COST"))
    print("------------------------------------------------------------------------------")
    
    
    Total = 0 
    
    for i in tickets:
        i.print_ticket()
        Total = Total + i.totalTicketCost

    print(f"\n\nYour order total: ${Total:.2f}")
    print("\nEnjoy your stay at Disneyland, the happiest place on earth!")

if __name__ == "__main__":
    main()

    
    
    
    
    
    
        
        
        
        
        
        


