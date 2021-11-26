# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

numShoes = int(input())
shoes = Counter(map(int,input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size,prize = map(int,input().split())
    if(shoes[size]):
        income +=prize
        shoes[size] -= 1
print(income)