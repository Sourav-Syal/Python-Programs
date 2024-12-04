L1 = [4,2,5,63,67,98]
L2 = [34,32,43,54,65,2]

square_ven = [(x*x,y*y) for (x,y) in zip(L1,L2) if x % 2 == 0 and y % 2 == 0]
print(square_ven)