import random

def is_prime(n, k=10):
    #we just care about positive integers
    if n <= 1:
        return False
    
    for iteration in range(k):
        #generate a random number [2, N-1]
        a = random.randint(2, n)-1
        
        #if a^n - 1 % n != 1 then n is not a prime
        if pow(a, n-1, n) != 1:
            return False
    
    #after k iterations we can come to the conclusion that n is a prime
    return True

if __name__ == "__main__":
    print(is_prime(99194853094755497)) 