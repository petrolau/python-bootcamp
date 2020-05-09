nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[0][1])

#nested list comprehension
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
[[print(val) for val in l] for l in nested_list]

board = [[num for num in range (1,4)] for val in range(1,4)]
print(board)
board2 = [["X" if num%2 == 0 else "O" for num in range (1,4)] for val in range (1,4)]
print(board2)
board3 = [ ["*" for x in range (1,4)] for i in range (1,4)]
print(board3)