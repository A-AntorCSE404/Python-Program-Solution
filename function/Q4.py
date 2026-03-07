def main():
    
    # generate the list
    numbers = list(range(1, 11))

    # squared store the square of the each numbers
    squared = map(lambda x: x**2, numbers)

    # filtered only stored where squared is greater than 25
    filtered = filter(lambda x: x > 25, squared)

    # print the filtered list
    print(list(filtered))

if __name__=="__main__":
    main()

