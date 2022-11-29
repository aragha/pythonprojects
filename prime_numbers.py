import math


def check_prime(n):
    """
    input: any number
    output: boolean True if the number is prime
    boolean False if the number is not prime
    """
    root = int(math.sqrt(n))
    # print(root)
    for i in range(2, root + 1):
        if n % i == 0:
            return False

    return True

# print(check_prime(88))
# prime_list = []
# print("Prime          Not Prime")
# for i in range(2, 1000):
#     if check_prime(i):
#         print(i)
#         prime_list.append(i)
#     else:
#         print(f"               {i}")
# print(prime_list)
