import numpy as np

def sigmoid(x):
    exp_x = np.exp(-x)
    return 1/(1 + exp_x)

print(sigmoid(1))
print(sigmoid(2))
