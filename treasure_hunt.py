import random
grid=[]

#start a function to start the grid
def start_grid():
    for r in range(4):
        row=[]
        for c in range(4):
            row.append("X")
        grid.append(row)
    return grid
#place treasure
def place_treasure():
    row=random.randint(0,4)
    col=random.randint(0,4)
    return (row,col)
#hints
def hints(tr,gr,tc,gc):
    if gr>tr:
        return "Move Up"
    elif gr<tr:
        return "Move Down"
    elif gc>tc:
        return "Move Left"
    elif gc<tc:
        return "Move Right"
    return "You found the treasure!"
#gameplay
def treasure_hunt():
    grid=start_grid()
    tr,tc=place_treasure()
    print("Welcome to the Treasure Hunt!")
    attempts=0
    #main game loop
    while True:
        print("\nCurrent Grid:")
        for row in grid:
            print(" ".join(row))
        #user guess
        try:
            gr=int(input("Enter your guess for row (0-4): "))
            gc=int(input("Enter your guess for column (0-4): "))
        except ValueError:
            print("That is not a number from 0-4")
            continue
        if gr not in range(5) or gc not in range(5):
            print("That is not a number from 0-4")
            continue
        attempts=attempts+1
        #check guess
        if gr==tr and gc==tc:
            print("Congratulations! You found the treasure in {} attempts!".format(attempts))
            break
        else:
            print("incorrect")
            hint=hints(tr,gr,tc,gc)
            print("Hint: {}".format(hint))
treasure_hunt()
