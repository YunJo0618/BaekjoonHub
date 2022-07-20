T = int(input())
list = []

for i in range(T):
    A, B = map(int, input().split())
    #print("Case #%d: %d"%(i+1, A+B))
    list.append(A + B)

for i in range(len(list)):
    print("Case #%d: %d"%(i+1, list[i]))
