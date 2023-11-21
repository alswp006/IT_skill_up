# 백준 18352번 특정 거리의 도시 찾기

# idea
# 각 노드간의 거리를 1로 두고 다익스트라 알고리즘을 통해 출발 노드에서 각 노드까지의 거리를 구한다.

import sys
import heapq

input = sys.stdin.readline
INF = 1e9

n, m, target_distance, start = map(int,input().split())

table = [INF] * (n + 1)
table[start] = 0
arr = [[] for _ in range(n+1)]
heap = []
heapq.heappush(heap, [0, start])
answer=[]

for _ in range(m):
    starting_node, destination_node = map(int,input().split())
    arr[starting_node].append([1, destination_node])

def dijkstra():
    while heap:
        v, w = heapq.heappop(heap)
        for next_dist, next_node in arr[w]:
            update = next_dist + v
            if update < table[next_node]:
                table[next_node] = update
                heapq.heappush(heap, [update, next_node])

dijkstra()

has_answer = False

for i in range(1, len(table)):
    if table[i] == target_distance:
        print(i)
        has_answer = True

if not has_answer:
    print(-1)