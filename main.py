def factorial(n):
    if not n.isnumeric():
        print("not a number")
        return
    n = int(n)
    if n < 0:
        print("number nust be positive")
        return

    res = 1
    for i in range(1, n):
        res *= i
    return res


def fibonacii(n):
    if type(n) != int and not n.isnumeric():
        print("not a number")
        return
    n = int(n)
    if n < 0:
        print("number nust be positive")
        return
    if n > 100:
        print("number too big")
        return

    if n == 1 or n == 2:
        return 1

    return fibonacii(n - 1) + fibonacii(n - 2)


def gcd(num1, num2):
    if not num1.isnumeric() or not num2.isnumeric():
        print("not a number")
        return
    num1, num2 = int(num1), int(num2)

    for i in range(min(num1, num2), 1, -1):
        if num1 % i == num2 % i == 0:
            return i
    return 1


def main():
    # num = input("enter a number ")
    # print("factorial", factorial(num))
    #
    # num = input("enter a number ")
    # print("fibonacii", fibonacii(num))
    #
    # num1, num2 = input("enter 2 numbers \n"), input()
    # print("gcd", gcd(num1, num2))
    s = "12345 + 5551 "
    ls = s.split()
    print(ls)

if __name__ == '__main__':
    main()
