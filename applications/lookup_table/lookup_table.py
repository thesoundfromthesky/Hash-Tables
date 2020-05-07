import math
import random

cache={}

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    cur=f"{x},{y}"
    if cur in cache:
        return cache[cur]

    v = math.pow(x, y)
    v = math.factorial(v)
    cache[cur]=None
        
    v //= (x + y)
    v %= 982451653
    cache[cur]=v

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
