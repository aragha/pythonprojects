from prime_numbers import check_prime

# Press the green button in the gutter to run the script.
print("Prime          Not Prime")
if __name__ == '__main__':
    for i in range(2, 1000):
        if check_prime(i):
            print(i)
        else:
            print(f"               {i}")