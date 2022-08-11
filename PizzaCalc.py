import math

def calc_circumference(radius):
    return 2 * math.pi * radius; 

def calc_area (radius):
    return math.pi * radius*radius;


def calc_diameter (radius) : 
    return 2 * radius; 
    
    

def main ():
    
    print("Welcome to the last pizza calculator you will ever need")
    diam = int(input("\nEnter pizza size (e.g., 12in, 18in): "))
    Num_G = int(input("\nEnter number of expected guests: "))
    
    radius = diam / 2 
    
    area = calc_area (radius)
    
    slicesPerPizza = area / 14.125
    
    slicesNeeded = Num_G * 2 
    
    numPizzas = math.ceil(slicesNeeded / slicesPerPizza)
    
    pizzaCirc = calc_circumference (radius)

    cupsCheese = math.ceil(pizzaCirc / 80) * numPizzas
    
    print (f"\n\nMake {numPizzas} pizzas to feed {Num_G} people.")
    print (f"\nBe sure to order {cupsCheese} cups of extra cheese to stuff the crust.")

if __name__ == "__main__":
    main()


    

