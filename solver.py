board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(pb):

    # Insert 'print(pb)' to watch backtracking steps

    # Return True if there aren't any more 0s to find
    find = find_zero(pb)
    if not find:
        return True  # Base Case of Recursion
    else:
        row, col = find

    for i in range(1,10):  # Loop through values 1-9
        if valid(pb, i, (row, col)):  # If values 1-9 would be valid | Pos: (row, col)
            pb[row][col] = i  # If valid, it will be added to the board

            if solve(pb):
                return True
            else:
                pb[row][col] = 0  # Backtrack, reset last position to 0, and return to previous position

    return False


def valid(pb, num, pos):

    # Check row
    for i in range(len(pb[0])):
        if pb[pos[0]][i] == num and pos[1] != i:  # Check if there are no duplications in that row
            return False

    # Check column
    for i in range(len(pb)):
        if pb[i][pos[1]] == num and pos[0] != i:  # Check if there are no duplications in that column
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if pb[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(pb):

    for i in range(len(pb)):
        # Separates board every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # Separates board every 3 positions in row
        for j in range(len(pb[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # \n at last position
            if j == 8:
                print(pb[i][j])
            else:
                print(str(pb[i][j]) + " ", end="")


# Backtrack if position = 0
def find_zero(pb):
    for i in range(len(pb)):
        for j in range(len(pb[0])):
            if pb[i][j] == 0:
                return i,j  # (Row,Column)
    return False


print("Before: ")
print_board(board)
solve(board)
print("\nAfter:")
print_board(board)
