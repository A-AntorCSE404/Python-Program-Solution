def dec_to_bin(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return dec_to_bin(n // 2) + str(n % 2)

# program entry point
if __name__=="__main__":
    for num in [0, 1, 10, 42, 255]:
        print(f"{num:>3} => {dec_to_bin(num)}")
