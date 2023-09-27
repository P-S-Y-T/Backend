#Tic Tac Toe
x = int(input("Enter the length of the sides in the Tic Tac Toe Layout :"))
for i in range(1,x):
    print("  |" * (x-1))
    print("-- " * x)
print("  |" * (x-1))

