"""Write a function in python that returns the largest prime factor of a given number."""
def answer(n):
    """function  that returns the largest prime factor of a given number."""
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
