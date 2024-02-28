# 1. 조건에 맞게 수열 변환하기
def solution(arr,k):
    if k % 2 != 0:
        return [i * k for i in arr]
    else:
        return [i + k for i in arr]

# 2. A강조 하기
def solution2(myString):
    return myString.lower().replace('a','A')