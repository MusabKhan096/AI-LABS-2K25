import numpy as np
A = np.array([[5, 5],[1, 2]])
B = np.array([[0, 1],[1, 0]])
result = A @ B  
print("==========")
print("Result:\n", result)
print("==========")
print("Transpose:\n", result.T)
print("==========")