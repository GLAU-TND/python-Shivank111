
n = int(input())
r = list(map(int,input().split()))
l = []
for i in r:
    l.append(r.count(i))
print(max(l))