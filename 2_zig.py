

def func(l,k,arr):
    for i in range(l,k):
        for j in range(l,k) :
            if i == l or j == l or j ==k-1 or i == k-1:
                arr[i][j]=l+1
    #pass
def zig(n):
    print(n)
    a_1 = 2*n-1

    arr = [[None] * a_1 for _ in range((a_1))]

    for i in range(0,n):
        ler=a_1-i
        print(ler)
        func(i,ler,arr)

    for i in arr:
        print(i,'\n')



zig(int(input('вести число')))
