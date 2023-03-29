import sys
input = sys.stdin.readline

n = int(input())
num_list = [0,1,2,3,4,5,6,7,8,9] # 여기서 값을 뽑아서 쓸거다.
alphabet_list = []
alphabet_dict = dict()
result = 0

for i in range(n):
    alphabet_list.append(input().rstrip()) # \n이 추가로 들어오기 때문에 .rstrip()을 해준다.

for alphabets in alphabet_list:
    for index in range(len(alphabets)):
        if alphabets[index] in alphabet_dict:
            alphabet_dict[alphabets[index]] += 10**(len(alphabets)-index-1)
        else:
            alphabet_dict[alphabets[index]] = 10**(len(alphabets)-index-1)

alphabet_values = sorted(list(alphabet_dict.values()), reverse=True)
for i in range(len(alphabet_values)):
    result += alphabet_values[i]*num_list.pop()
print(result)