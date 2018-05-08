grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]
        
def tGrid(grid):
    nGrid = []
    for x in range(len(grid[0])):
        nGrid.append([])
        if x != 0:
            # pass
            print()
        for y in range(len(grid)):
            # pass
            nGrid[x].append(grid[y][x])
            # print(grid[y][x],end='')

    for y in range(len(nGrid)):
        if y != 0:
            pass
            # print()
        for x in range(len(nGrid[0])):
            print(nGrid[y][x],end='')
    return nGrid

print(tGrid(grid))
# tGrid(grid)

input()