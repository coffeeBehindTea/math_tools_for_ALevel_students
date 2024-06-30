import os
def factorial(n):
    #! 递归求阶乘
    if n == 0:
        return 1

    return n * factorial(n - 1)


def Binomial(a, b, n, r):
    # 求第n项的系数
    fir = factorial(n) / (factorial(r) * factorial(n - r))
    sec = a ** (n - r)
    thr = b ** r
    return float(fir * sec * thr)


def mutiBinomial(times, a, b, n):
    # 求多次第n项的系数
    ans = []
    for i in range(times):
        ans.append(Binomial(a, b, n, i))
    return ans


def modeChoice():
    mode = int(input("mode(1单2多) "))

    if mode == 1:
        # 输入
        print("=======MODE1======")
        a = float(input("a= "))
        b = float(input("b= "))
        n = int(input("n= "))
        r = int(input("r= "))
        print("=======OUTPT======")
        print(Binomial(a=a, b=b, n=n, r=r))
    elif mode == 2:
        # 输入
        print("=======MODE2======")
        a = float(input("a= "))
        b = float(input("b= "))
        n = int(input("n= "))
        times = int(input("firt___times: "))
        print("=======OUTPT======")
        print(mutiBinomial(times=times, a=a, b=b, n=n))

# 主函数
if __name__ == "__main__":
    while 1:
        modeChoice()
        _ = input("按任意键继续...")
        os.system("cls")