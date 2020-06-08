# Your code here
import math
import random
cache ={}

def build_lookup_table():
	for x in range(50000):
		cache[x] = math.factorial(x)
# creating the lookup table. for every iteration x in the range from 0 to 49999, set the key to cache[x] and the value to the factorial of x.

# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = math.pow(x, y)
    # v = math.factorial(v)

    if v not in cache:
        cache[v] = math.factorial(v)
    v = cache[v]
    v //= (x + y)
    v %= 982451653
    
    return v



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
