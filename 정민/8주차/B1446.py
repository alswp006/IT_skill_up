# 백준 1446번 

import sys
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(10001)]

for _ in range(n):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

distance = [i for i in range(d + 1)]

print(graph)
print(distance)

for i in range(d + 1):
  distance[i] = min(distance[i], distance[i-1]+1)
  for 


# found = False
# for i in range(1, n + 1):
#   if distance[i] == 150:
#     print(i)
#     found = True

# if not found:
#   print(-1)
  