fi = r"C:\Users\rajatx\Documents\python\Network_Projects\dict1.txt"
matchword1 = "subnet_name"
matchword2 = "cidr_block"
print("!"*50)
with open(fi,"r+") as file:
    for file in file:
        if matchword2 in file:
            b = file
            print(b,sep="",end="")
        if matchword1 in file:
            a= file
            print(a,sep="",end="")
            print("!"*50)        


    
