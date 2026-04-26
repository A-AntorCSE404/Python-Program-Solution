import os

def country(city):

    with open("world_data.txt","r") as f:
        data = f.readlines()

        for line in data:
            line = line.strip()         # remove newline space
            line = line.split(",")         # split by comma
            
            if city in line:
                print(f"[Found]: {city} belongs to {line[0]}")
                break
        else:
            print(f"[Missing]: {city} not in the database")

def main():

    # check file path exists or not ?
    filepath = os.path.exists("/home/silentRoot6910/Python/FileHandling/world_data.txt")

    if filepath:
        city = input("Enter the City name:")
        country(city)       # check city belongs to which country

    else:
        print("File Not Found")


if __name__=="__main__":
    main()
           
