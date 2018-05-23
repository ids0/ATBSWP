tableData =[['apples','oranges','cherries','banana'],
            ['Alice','Bob','Carol','David'],
            ['dogs','cats','moose','goose']]

def printTable(table):
    rows = len(table[0])            # Number of rows to print
    col = len(table)                # Number of columns to print
    colWith = [0] * len(table)      # A list of the same number of items as columns to print, will be used to save the longest strin in each column
    for c in range(col):            # Iterates in every column to find the longes string 
        longest = 0                 # Every time the loop adds 1 it resets the count
        for r in range(rows):    # Iterates every strig in every list, it also can be done with 'item in talbe[c]'
            if len(table[c][r]) > longest: 
                longest = len(table[c][r])   
        colWith[c] = longest    # Saves the length of the longest string in order
    for r in range(rows):       # Same principle as in the printT first the rows act as columns
        if r != 0:              # First line without new line
            print()             
        for c in range(col):    
            print(table[c][r].rjust(colWith[c]),end=' ') # [c][r] is a must, becouse table has only 'c' items and table[c] has 'r'items
        

printTable(tableData)
input()
