s='abcdefghij'
print(s.index("a")) # found the location of the a using index
print(s.replace("a","A")) # changed the small a to A

print("*" * 40)
for i in range(3):
    print("*", " "*36 , "*")

print("*" * 40)

for i in range(4):
    print("*")
    for j in range(3):
        print("*",sep="")
        
print("-"*30)
rows =4
for i in range(1, rows + 1):
    print("1" * i)       
print("-"*30)
for i in range(1, 5):
    print("*" * i)       


# Number of rows in the pyramid
rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print '1's in increasing pattern
    print("1" * (2 * i - 1))
