import random
grid=[]
#start a function to start the grid
def start_grid():
    for r in range(10):
        row=[]
        for c in range(10):
            row.append("X")
        grid.append(row)
    return grid
#place treasure
def place_treasure():
    row=random.randint(0,9)
    col=random.randint(0,9)
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
    score=0
    print("Welcome to the Treasure Hunt!")
    attempts=0
    #main game loop
    while True:
        print("\nCurrent Grid:")
        for row in grid:
            print(" ".join(row))
        #user guess
        try:
            gr=int(input("Enter your guess for row (0-9): "))
            gc=int(input("Enter your guess for column (0-9): "))
        except ValueError:
            print("That is not a number from 0-9")
            continue
        if gr not in range(10) or gc not in range(10):
            print("That is not a number from 0-9")
            continue
        attempts=attempts+1
        #check guess
        if gr==tr and gc==tc:
            print("Congratulations! You found the treasure in {} attempts!".format(attempts))
            score+=3.141592
            break
        else:
            print("incorrect")
            score=score-1
            hint=hints(tr,gr,tc,gc)
            print("Hint: {}".format(hint))
    print("Your final score is {}".format(score))
treasure_hunt()