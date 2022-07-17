# 백준11170 (0의 개수 세기)
# 숫자를 리스트에 저장해서 0의 개수 출력

for _ in range(int(input())):
    N, M = map(int, input().split())
    SUM = 0
    for i in range (N, M+1):
        NUM = list(str(i))
        if '0' in NUM:
            SUM += NUM.count('0')
    print(SUM)

# 백준 11655 (알파벳 13씩 밀어서 출력)

TEXT = list(input())
TEXT1 = []

for i in TEXT:
    if i.isalpha(): #알파벳인지 확인
        if i.isupper():
            TEXT1.append(chr(65+(ord(i)+13-65)%26))
        else:
            TEXT1.append(chr(97+(ord(i)+13-97)%26))
    else:
        TEXT1.append(i)
print(*TEXT1, sep="")

