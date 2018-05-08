#     'x' 0   1   2   3   4   5     # Y
grid = [['.','.','.','.','.','.'],  # 0
        ['.','0','0','.','.','.'],  # 1
        ['0','0','0','0','.','.'],  # 2
        ['0','0','0','0','0','.'],  # 3
        ['.','0','0','0','0','0'],  # 4
        ['0','0','0','0','0','.'],  # 5
        ['0','0','0','0','.','.'],  # 6
        ['.','0','0','.','.','.'],  # 7
        ['.','.','.','.','.','.']]  # 8

def tGrid(grid):
    for x in range(len(grid[0])):       # len(grid[0]) == '6'
        if x != 0:
            print()                     # lnew line except for the first line
        for y in range(len(grid)):      # len(grid) == '9'
            print(grid[y][x],end='')    # firt iterates in X==0 and every Y of X == 0 is printed in the first line '..00.00..'    # print without a new line at the end
tGrid(grid)
input()