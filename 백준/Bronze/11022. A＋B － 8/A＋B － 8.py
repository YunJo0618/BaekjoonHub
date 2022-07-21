T = int(input())
list = []

for i in range(T):
    A, B = map(int, input().split())
    list.append(A + B)
    print("Case #%d: %d + %d = %d"%(i+1, A, B, list[i]))
 