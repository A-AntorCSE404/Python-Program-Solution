def read_file(filename):
    try:
        if filename == "ghost.txt":
            raise FileNotFoundError("No such file: ghost.txt")
        if filename == "secret.txt":
            raise PermissionError("Access denied: secret.txt")
        content = f"[Contents of {filename}] — Hello!"
    
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    
    except PermissionError as e:
        print(f"ERROR: {e}")
    
    else:
        print("Success:", content)
    
    finally:
        print("Session closed.\n")


if __name__=="__main__":
    read_file("data.txt")
    read_file("ghost.txt")
    read_file("secret.txt")
                                                                             
