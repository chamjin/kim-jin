# 백준10821 (정수의 개수)

a = list(map(int,input().split(',')))
print(len(a)) #콤마로 구분된 정수의 개수 세기

# 백준10808 (알파벳 개수)
# 이해 못함... 어려움

a = 'abcdefghijklmnopqrstuvwxyz'
b = [0] * len(a)
s = input()
for w in s:
    for i in range(len(a)):
        if w == a[i]:
            b[i] += 1
            break
print(*b)

# 백준1157 (단어 공부)
# 어려워서 사망

word = input().upper()
word_set = list(set(word))
cnt = []

for i in word_set:
    cnt.append(word.count(i))

if cnt.count(max(cnt))>1 :
    print("?")
else:
    print(word_set[cnt.index(max(cnt))])

# 백준5218 (알파벳 거리)
# 오바임

for _ in range(int(input())):
    a, b = input().split()
    li = []
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            li.append(26 - (ord(a[i])-ord(b[i])))
        else:
            li.append(ord(b[i]) - ord(a[i]))
    print("Distances:", *li)

# 백준9086 (첫번째 문자랑 마지막 문자만 출력)

T = int(input())

for _ in range (T):
    A = input()
    print(A[0], A.strip()[-1], sep = "")

# 백준11365 (문자열 뒤집기)

N = True
while N:
    A = input()
    if A == "END":
        N = False
    else:
        print(A[::-1]) #문자열이 뒤집어짐