#백준 4796번 캠핑

#idea
#V//P*L+V%P를 해준다.

import sys

count = 1
while True:
    L,P,V=map(int,sys.stdin.readline().split())
    if L==0: break
    if V%P<=L:
        print(f'Case {count}: {(V//P*L+V%P)}')
    else:
        print(f'Case {count}: {(V//P*L+L)}')
    count+=1