import sys

N = int(input())
person = []
addList = [1 for _ in range(N)] # 등수 리스트를 만들어줍니다.

for _ in range(N): # 각 인원들의 키, 몸무게 값을 리스트로 만들어줍니다.
    n = list(map(int, sys.stdin.readline().split()))
    person.append(n)

for i in range(0, N - 1): # 리스트를 비교합니다. n! ?
    for j in range(i + 1, N):
        if person[i][0] < person[j][0]:
            if person[i][1] < person[j][1]:
                addList[i] += 1
            else:
                pass
        elif person[i][0] > person[j][0]:
            if person[i][1] > person[j][1]:
                addList[j] += 1
            else:
                pass
# addList 값을 하나씩 증가시킨다 -어떨때? - 왼쪽이 다 크던가 오른쪽이 다 크든가 할 때만
printed = ' '.join(str(s) for s in addList)
print(printed)