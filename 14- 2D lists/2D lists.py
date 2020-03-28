""" A 2D list is exactly a matrix. Each row is an element for the array """
number_grid = [
    [1,2,3],
    [2,4,5],
    [3,6,7],
    [4,8,9]
]

print(number_grid) #Print(array_name[array_row][row_character]) will print an individual 
print(number_grid[1][2])

for row in number_grid:
    print(str(row) +" <- Row")
    for number in row:
        print(str(number) + " <- Number")

 


 