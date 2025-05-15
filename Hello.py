def compute_prime_factors(n):
    """Compute the prime factors of a given number n."""
    i = 5 # This is an error
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print("This function was implemented by Pablo")
    return factors