D = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

Input = input()

for i in D:
    Input = Input.replace(i, '*')
    # i 와 동일한 문자를 * 로 바꿔줌

print(len(Input))