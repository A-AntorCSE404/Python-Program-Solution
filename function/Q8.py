def memoize(func):

    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    
    return wrapper


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)



if __name__=="__main__":
    
    # print a list of number fibonacci
    for i in [10,20,30,35]:
        print(f"fib({i}) = {fib(i)}")

