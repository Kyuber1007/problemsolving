import sys

input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
total_price = 0

for i, value in enumerate(distances):
    if prices[i] < min_price:
        min_price = prices[i]
    total_price += min_price * value
print(total_price)
