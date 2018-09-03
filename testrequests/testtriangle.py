
def print_tirangle(n):
    print("------------------------输出头————————————")
    print(1)
    for i in range(2, 2*n-1):
        print("————————第 %s 批输出—————————" % i)
        if i == n:
            for j in range(1, n+1):
                print(n*j-(j-1))
        elif i != n:
            # 绝对值
            num = abs(n-i)
            print("差值"+str(num))
            if n-i > 0:
                for k in range(0, i):
                    print(i+k*(n-1))
            elif n-i < 0:
                for k in range(0, 2*n-i):
                    print(n*(num+1)+k*(n-1))
    print("------------------------输出尾————————————")
    print(n*n)


print_tirangle(10)