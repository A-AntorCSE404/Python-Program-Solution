import time

def timer(func):

    def wrapper(*args, **kwargs):
        # initial starting time
        start = time.time()
        result = func(*args, **kwargs)
        #after calling big_sum function currently total time
        elapsed = (time.time() - start) * 1000  # multiply by 1000 to make the execution time in miliseconds.
        
        print(f"{func.__name__} ran in {elapsed:.2f} ms")
        return result

    return wrapper

@timer
def big_sum():
    return sum(range(1_000_000))

if __name__=="__main__":
    big_sum()

