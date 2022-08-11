
class DreamVacation:
   
    __destination: str 
    __description: str 
    __days: int
    __nights: int 
    __cost: float
    
    def __init__(self, dest, desc, d, ni, c):
            self.__destination = dest
            self.__description = desc
            self.__days = d
            self.__nights = ni
            self.__cost = c
    
    
    def print_vaca(self):
        print (f"\n\n---------SPECIAL OFFER--------")
        print(f"\n           {self.__destination}")
        print(f"\n{self.__description}")
        print(f"\n{self.__days} days, {self.__nights} nights") 
        print(f"\nStarting at: ${self.__cost:,.2f}")
        print("\nContact Alaa Musa for more details")
    
    
    @property
    def destination(self):
        return self.__destination
        
    @property
    def description(self):
        return self.__description
        
    @property
    def days(self):
        return self.__days
        
    @property
    def nights(self):
        return self.__nights
        
    @property
    def cost(self):
        return self.__cost
        
    @destination.setter
    def destination(self, newDest):
        self.__destination = newDest;
    
    @description.setter
    def description(self, newDesc):
        self.__description = newDesc;
    
    @days.setter
    def days(self, newD):
        self.__days = newD;
    
    @nights.setter
    def nights(self, newNi):
        self.__nights = newNi;
    
    @cost.setter
    def cost(self, newC):
        self.__cost = newC;
    
    
def main():
        
    r1 = DreamVacation("Ibiza", "Party all night and all day at the\n wonderful and one of a kind Ibiza!", 2, 3, 2500.00)
        
    r2 = DreamVacation("Nice, France", "The ultimate couples vacation, \nNice, France offers one of a kind views and food \nthat is sure to be memorable!", 5, 6, 5500.00)
        
    r1.print_vaca()
    r2.print_vaca()

main()
        
        
