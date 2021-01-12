#LRUD LEFT RIGHT UP DOWN
import time


## My answer

N = int(input())

LRUD = list(input().split())

START_POINT = [1,1]
start_time = time.time()
for direction in LRUD:
        if direction == "L":
            START_POINT[1] -= 1
        elif direction == "R":
            START_POINT[1] += 1
        elif direction == "U":
            START_POINT[0] -= 1
        elif direction == "D":
            START_POINT[0] += 1

        for index, point in enumerate(START_POINT):
            if point > N:
                START_POINT[index] = N
            elif point == 0 :
                START_POINT[index] = 1

end_time = time.time()
print("time:",end_time - start_time)

print(START_POINT[0], START_POINT[1])

### Ans

n = int(input())
x,y = 1,1
plans = input().split()

move_types =["L","R","U","D"]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
start_time = time.time()
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny
end_time = time.time()
print("time:",end_time - start_time)
#continue 구문: 반복문 안에서 continue 를 사용하면 continue 아래 구문은 실행하지 않고 다음 iteration으로 넘어감

print(x,y)

#두 code의 차이 : 예외처리의 방법 -> 사전처리와 사후일괄처리