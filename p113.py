import time

# N = int(input())
#"N:59:59"

## MY ANSWER
N = 6
cnt = 0
result = 0

COMPLEXITY = 0

def classifer(time,cnt):
    global COMPLEXITY
    str_i = str(time)
    if len(str_i) == 1:
        str_i = "0" + str_i
    if str_i[0] == "3" or str_i[1] == "3":
        cnt = 1
        COMPLEXITY +=1
    return cnt

start_time = time.time()
for k in range(N+1):
    cnt =classifer(k,cnt)
    if cnt != 0 :
        result += 3600
        cnt = 0
        continue
    for j in range(60):
        cnt = classifer(j,cnt)
        if cnt != 0 :
            result += 60
            cnt = 0
            continue
        for i in range(60):
            cnt = classifer(i,cnt)
            if cnt != 0 :
                result += 1
                cnt = 0
end_time = time.time()
print("time:",end_time - start_time)
print(result)
print(COMPLEXITY)

##ANS
COMPLEXITY = 0
count = 0
start_time = time.time()
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1
                COMPLEXITY +=1
end_time = time.time()
print("time:",end_time - start_time)
print(count)
print(COMPLEXITY)


# 내 코드의 장점: 시,분,초 중 최상위 단계에서 3이 발견되면 하위 단계의 탐색을 하지 않는다. 따라서 수행시간을 절반 가량으로 줄일 수 있다.
# N=5일 때 MY code: 0.012s, Ans code : 0.021s
