import numpy as np
arr = np.array([[1,2,3],[5,6,7],[9,8,7]])
arr1 = np.array([[(1,2,3), (4,5,6)],[(3,2,1), (4,5,6)]])

#print(np.zeros((3,4,5), dtype = "int"))
#print(np.ones(4))
#print(np.full((2,3),6,"int"))

#print(np.random.rand(3,2))

#print(np.random.randint(0,20,(3,3)))

np.random.seed(42)
#print(np.random.rand(4))

dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])
print(dice_rolls[dice_rolls>2].size)