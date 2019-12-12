def count_primes(num):
    prime_total = 0
    for prime_num in range(2, num + 1): 
        prime_counter = 0
        i = 1
        while i <= prime_num:
            if prime_num % i == 0:
                prime_counter += 1
                if prime_counter > 2:
                    break
                elif prime_counter == 2 and i == prime_num:
                    prime_total += 1
                i += 1
            else:
                i += 1
    return prime_total

# Check
count_primes(100)