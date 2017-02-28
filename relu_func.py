import numpy as np

def relu(x):
    return np.maximum(0, x)

print(relu(-1))
print(relu(0))
print(relu(1))
print(relu(100))
