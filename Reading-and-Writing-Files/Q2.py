import os

def main():

    # check file exists ?
    filepath = os.path.exists("/home/silentRoot6910/Python/FileHandling/world_data.txt")

    if filepath:
        with open("/home/silentRoot6910/Python/FileHandling/world_data.txt", "r") as f:
            data = f.readlines()

            for line in data:
                line = line.strip()         # remove newline spaces
                line = line.split(",")      # split by comma

                if "Asia" in line:
                    print(f"{line[0]} --> {line[1]}")


    else:
        print("file not found")



if __name__=="__main__":
    main()
