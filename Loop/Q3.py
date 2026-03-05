secret = (7,4,2) # secret key number 
found  = False   # flag
attempts = 0     # counter that counts how many has taken to retrive the secret key

for a in range(10):
    for b in range(10):
        for c in range(10):
            attempts +=1
            if (a,b,c) == secret:
                print("Secret PIN Cracked!")
                print("Secret key is:",str(a)+str(b)+str(c))
                found =True
                break
        if found == True:
            break  # exit from the second for loop
    if found == True:
        break   # exit from the most outer for loop
else:
    print("Secret Key Not Found!")
