row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

row = int(position[1])
col = int(position[0])

if row - 1 > 3:
    row = 3
if col - 1 > 3:
    col = 3

map[row-1][col-1] = '🏆'

print(f"{row1}\n{row2}\n{row3}")