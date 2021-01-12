import time
#My Ans
N, M = map(int,input().split())
x, y, dir = map(int, input().split())
# direction : 0->N, 1->E, 2->S ,3->W
## 2차원 array 입력받는 방법

MAP = []
for i in range(N):
    TEMP = list(map(int,input().split()))
    MAP.append(TEMP)

# N,M,x,y,dir = 4,4,1,1,0
# MAP = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# N,E,S,W
dx = [0,1,0,-1]
dy = [-1,0,1,0]
result = 1
cnt = 0
while True :
        TEMP_x = x + dx[dir]
        TEMP_y = y + dy[dir]
        if TEMP_x >= 1 and TEMP_x < N and TEMP_y >= 1 and TEMP_y < M and MAP[TEMP_y][TEMP_x]==0:
            MAP[y][x] = 2
            x = TEMP_x
            y = TEMP_y
            result +=1
            cnt = 0
        else :
            cnt += 1
            if cnt == 4 :
                x = x - dx[dir]
                y = y - dy[dir]
                cnt = 0
                if MAP[y][x] == 1:
                      break
            dir -= 1
            if dir == -1:
                dir = 3
print(result)

##정답과 idea가 동일함.