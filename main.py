from prime_numbers import check_prime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(2, 200):
        if check_prime(i):
            print(i)