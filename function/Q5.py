def apply(func, value):
    return func(value)

# lambda function
double = lambda x: x * 2

# program entry point
if __name__=="__main__":
    result = apply(double, 21)
    print(result)
                    
