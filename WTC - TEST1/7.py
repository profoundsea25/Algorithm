new_grid = []

def cw(grid) :
    global new_grid
    n = len(grid)
    last = []

    for i in range(n-1,-1,-1):
        last.append(grid[i][-1])
        if len(grid[i]) == 1 :
            grid[i] = []
        else :
            grid[i] = grid[i][:-1]
            last.append(grid[i][-1])
            grid[i] = grid[i][:-1]
    
    grid.pop(0)
    new_grid.insert(0, last)
    if grid :
        cw(grid)
    else :
        return

def ccw(grid) :
    global new_grid
    n = len(grid)
    last = []

    for i in range(n-1,-1,-1):
        last.append(grid[i][0])
        if len(grid[i]) == 1 :
            grid[i] = []
        else :
            grid[i] = grid[i][1:]
            last.append(grid[i][0])
            grid[i] = grid[i][1:]
    
    grid.pop(0)
    last.reverse()
    new_grid.insert(0, last)
    if grid :
        ccw(grid)
    else :
        return

def solution(grid, clockwise):
    if clockwise :
        cw(grid)
    else :
        ccw(grid)
    for i in range(len(new_grid)):
        new_grid[i] = ''.join(new_grid[i])
    return new_grid


#grid = ["1","234","56789"]
grid = ["A","MAN","DRINK","WATER11"]
#clockwise = True
clockwise = False
print(solution(grid,clockwise))
