import os

def main():

    # check numbers.txt file is exists ?
    filepath = os.path.exists("/home/silentRoot6910/Python/numbers.txt")

    if filepath:
        
        with open("/home/silentRoot6910/Python/numbers.txt", "r") as f:
            
            data = f.readlines()

            for line in data:
                line = line.strip()         # remove newline spaces
                nums =line.split(",")       # split by comma

                total =0
                for n in nums:
                    total +=int(n.strip())  #remove spaces and convert to int

                print(total)
                
    else:
        print("File not Found")

if __name__=="__main__":
    main()
