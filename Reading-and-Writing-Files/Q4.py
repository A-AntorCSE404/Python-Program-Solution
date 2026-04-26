import os

def main():

    # check world_data.txt file exists or not ?
    filepath = os.path.exists("/home/silentRoot6910/Python/FileHandling/world_data.txt")
  
    if filepath is not True:
        print("file is not found")

    # read world_data.txt fiel
    with open("world_data.txt", "r") as file:
        lines = file.readlines()

    
    # overwrite the world_data.txt file 
    with open("world_data.txt", "w") as file:
        for line in lines:
            if line.strip() == "USA,Washington DC,North America":
                file.write("USA,New York City,North America\n")
            else:
                file.write(line)

if __name__=="__main__":
    main()
