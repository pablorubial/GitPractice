def compute_prime_factors(n):
    """Compute the prime factors of a given number n."""
    i = 2
    factors = []
    while i * i <= n:
        print(f"Current i: {i}, Current n: {n}") # This is Max's debug step
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print("This function was implemented by Pablo")
    return factors
