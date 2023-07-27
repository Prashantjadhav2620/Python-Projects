import getpass

data={"prashant.jadhav":"prashant6@" ,"sushant.jadhav":"susu9089@"}

username = input("Enter Your User Name : ")

password = getpass.getpass("Enter Your Password : ")

for i in data.keys():
    if username==i:
        while password !=data.get(i):
            password = getpass.getpass("Enter Your Password Again :")
        break
    
print("Verified")        

# OutPut: -
#     Enter Your User Name : prashant.jadhav
# Enter Your Password : 
# Enter Your Password Again :
# Enter Your Password Again :
# Enter Your Password Again :
# Enter Your Password Again :

# Verified