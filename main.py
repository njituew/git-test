def main():
    n, k, d = map(int, input().split())
    flag = False
    for digit in range(10):
        if (n * 10 + digit) % k == 0:
            n = n * 10 + digit
            flag = True
            break

    if not flag:
        print(-1)
    else:
        print(n, end="")
        [print(0, end="") for _ in range(d-1)]


if __name__ == "__main__":
    main()
