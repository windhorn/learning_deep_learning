import numpy as np

def step_func(x):
    y = x > 0
    return y.astype(np.int)


print(step_func(np.array([-1.0, 1.0, 2.0])))
print(step_func(np.array([0.0, 1.0])))
