#백준 7785번 회사에 있는 사람

#idea
#

import sys

input=sys.stdin.readline

di = dict()
for _ in range(int(input())):
    n,m=map(str,input().split())
    if m=='enter':
        di[n]=1
    else:
        del di[n]

for i in sorted(di.keys(), reverse=True):
    print(i)