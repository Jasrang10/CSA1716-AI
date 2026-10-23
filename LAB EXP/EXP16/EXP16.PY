
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Inputs
x1, x2 = 1, 0

# Weights
w1, w2 = 0.5, 0.8
bias = 0.1

# Feed forward calculation
hidden = sigmoid(x1 * w1 + x2 * w2 + bias)
output = sigmoid(hidden * 1.2 + 0.2)

print("Hidden Layer Output:", round(hidden, 4))
print("Final Output:", round(output, 4))
