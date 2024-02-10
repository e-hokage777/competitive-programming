stops = int(input())
current = 0
capacity = 0
for i in range(stops):
    left, entered = map(int, input().split())
    current += (entered - left)
    
    if current > capacity:
        capacity = current
        
print(capacity)