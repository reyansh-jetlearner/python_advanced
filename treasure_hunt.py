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

def hint(tr,gr,tc,gc):
    if gr>tr:
        return "Move Up"
    elif gr<tr:
        return "Move Down"
    elif gc>tc:
        return "Move Left"
    elif gc<tc:
        return "Move Right"