def answer(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == "__main__":
    number = int(input("enter the number"))
    print(answer(number))
