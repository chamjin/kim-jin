# 백준4458 (첫 글자를 대문자로)

T = int(input())

for _ in range (T):
    a = input()
    print(a[0].capitalize(),a[1:],sep="") #capitalize => 대문자 변환 함수

# 백준11654 (아스키 코드)

a = input()

if type(a) == str:
    print(ord(a))
elif type(a) == int:
    print(chr(a))

# 백준11720 (숫자의 합)

T = int(input())
number = int(input())
print(sum(map(int, str(number))))

# 백준 11721 (10글자씩 끊어 출력하기)

a = input()
for i in range(0, len(a), 10):
    print(a[i:i + 10])
