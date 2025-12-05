def cupstograms(cups,cr):
    return cups*cr

def tbsptotsp(tbsp):
    return tbsp*3

def granstocups(grams,cr):
    return grams/cr

def recipe_converter():
    print("Welcome to the Recipe Converter") 

    while True:
        print("Choose an option:")
        print("1. Cups to Grams")
        print("2. Grams to Cups")
        print("3. Tablespoons to Teaspoons")
        print("4. Exit")
    
        choice=int(input("Enter your choice (1-4): "))
    
        if choice==1:
            cups=float(input("Enter the number of cups: "))
            cr=float(input("Enter the grams per cup: "))
            result=cupstograms(cups, cr)
            print("{} cups is equal to {} grams.".format(cups,result))    
        
        elif choice == 2:
            tbsp=float(input("Enter the number of tablespoons: "))
            result=tbsptotsp(tbsp)
            print("{} tablespoons is equal to {} teaspoons.".format(tbsp,result))
    
        elif choice == 3:
            grams=float(input("Enter the number of grams: "))
            cr=float(input("Enter the grams per cup: "))
            result=granstocups(grams, cr)
            print("{} grams is equal to {} cups.".format(grams,result))
        
        elif choice == 4:
            print("Exiting the Recipe Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

recipe_converter()