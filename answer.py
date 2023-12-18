""" What is the largest prime factor of the number 600,851,475,143?"""
def answer(n):
    """function for largest prime factor of the number 600,851,475,143"
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == "__main__":
    print(answer(600851475143))
