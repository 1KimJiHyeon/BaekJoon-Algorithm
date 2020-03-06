# # 나의 답
# T = int(input())

# for i in range (T):
#     k = int(input())
#     n = int(input())
#     sum=0
#     for j in range (1,n+1):
#         sum+=(j+((k-1)*14))
#     print(sum)

# 답

T=int(input())
arr=[None]*14
newarr=[None]*14
for i in range(T):
    k=int(input())
    n=int(input())
    for z in range(k+1):
        for x in range(n):
            if z==0:
                arr[x]=x+1
                continue
            else:
                if x==0:
                    newarr[x]=1
                else:
                    newarr[x]=arr[x]+newarr[x-1]
        if(z!=0):
            arr=newarr
    print(arr[n-1])