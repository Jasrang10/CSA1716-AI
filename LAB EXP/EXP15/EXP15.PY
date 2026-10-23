
from math import *

data = [
    ['Sunny', 'No'],
    ['Sunny', 'No'],
    ['Rainy', 'Yes'],
    ['Rainy', 'Yes'],
    ['Cloudy', 'Yes']
]

tree = {}

for weather, play in data:
    if weather not in tree:
        tree[weather] = []
    tree[weather].append(play)

for weather in tree:
    tree[weather] = max(set(tree[weather]),
                        key=tree[weather].count)

print("Decision Tree:")
for weather, decision in tree.items():
    print(weather, "->", decision)

weather = input("Enter weather (Sunny/Rainy/Cloudy): ")
print("Decision:", tree.get(weather, "Unknown weather"))
