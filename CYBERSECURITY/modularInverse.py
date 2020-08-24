from math import sqrt
from math import floor

def modular_inverse(a, m):
    #this is the brute-force approach: we check all the values within the range [0, m-1]
    #problem: m may be too large (usually we use 1024 bits long prime number)
    #running time complexity it seems O(m) linear but it is exponential as far as the input bits are concerned
    for inv in range(0, m):
        if(a * inv) % m == 1:
            return inv
    
    print("there is no modular inverse (a is not a coprime to m)")

if __name__ == "__main__":
    #print(modular_inverse(7, 31))
    print(modular_inverse(6546542342343243211, 1212434445))