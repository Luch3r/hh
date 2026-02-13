import math

def find_mysterious_number(n):
    lcm = 1
    for i in range(2, n + 1):
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

print(find_mysterious_number(5))
print(find_mysterious_number(10))
