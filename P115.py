import time

##MY_ANS
POINT = input()

ROW = int(POINT[1])
COL = ord(POINT[0]) - 96 ## ASCII code

ROW_KNIGHT = [-1,-2,-2,-1,1,2,2,1]
COL_KNIGHT = [-2,-1,1,2,2,1,-1,-2]
result = 0
for i in range(8):
    KNIGHT_MOVE_ROW = ROW - ROW_KNIGHT[i]
    KNIGHT_MOVE_COL = COL - COL_KNIGHT[i]
    if KNIGHT_MOVE_ROW >=1 and KNIGHT_MOVE_ROW <=8 and KNIGHT_MOVE_COL >= 1 and KNIGHT_MOVE_COL <= 8:
            result +=1
print(result)


##ANS

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,-2),(-2,1)]

reult = 0
for step in steps:
    next_row = row +step[0]
    next_column = column +step[1]

    if next_row >=1 and next_row <=8 and next_column >=1 and next_column<=8:
        result +=1

print(result)


## 내 답과 ANS가 거의 유사하다.