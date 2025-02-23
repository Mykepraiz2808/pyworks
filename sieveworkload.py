def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_num + 1) if is_prime[p]]
    return primes

def main():
    max_num = 8191  # Lists all primes up to MaxNum
    num_iterations = 10  # Repeats procedure NumIterations times

    print(f'Using Eratosthenes Sieve to find primes up to {max_num}')
    print(f'Repeating it {num_iterations} times.')

    for iteration in range(1, num_iterations + 1):
        primes = sieve_of_eratosthenes(max_num)
        num_primes = len(primes)
        print(f'{num_primes} primes')

if __name__ == "__main__":
    main()
