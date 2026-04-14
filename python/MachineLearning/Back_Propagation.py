import numpy as np

# 1. Activation Function: Logistic (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 2. Derivative of Sigmoid for Backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# 3. Initial Inputs and Targets [cite: 24]
inputs = np.array([0.05, 0.10])
targets = np.array([0.01, 0.99])

# 4. Initial Weights and Biases [cite: 25]
# Weights for Hidden Layer (w1, w2, w3, w4)
weights_h = np.array([[0.15, 0.20], [0.25, 0.30]]) 
# Weights for Output Layer (w5, w6, w7, w8)
weights_o = np.array([[0.40, 0.45], [0.50, 0.55]]) 

bias_h = 0.35  # B1 [cite: 25]
bias_o = 0.60  # B2 [cite: 25]

learning_rate = 0.5

# 5. Training Loop: 10,000 iterations 
for i in range(10001):
    # --- Forward Pass ---
    # Hidden Layer calculation [cite: 28, 29, 30]
    hidden_layer_input = np.dot(inputs, weights_h.T) + bias_h
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    # Output Layer calculation [cite: 31, 32]
    output_layer_input = np.dot(hidden_layer_output, weights_o.T) + bias_o
    final_output = sigmoid(output_layer_input)
    
    # Calculate Error [cite: 33]
    error = 0.5 * np.sum((targets - final_output) ** 2)
    
    # --- Backward Pass --- [cite: 34, 38]
    # Error at Output Layer
    error_output = targets - final_output
    delta_output = error_output * sigmoid_derivative(final_output)
    
    # Error at Hidden Layer
    error_hidden = delta_output.dot(weights_o)
    delta_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)
    
    # Update Weights [cite: 36, 59]
    weights_o += np.outer(delta_output, hidden_layer_output) * learning_rate
    weights_h += np.outer(delta_hidden, inputs) * learning_rate

    # Print results every 2000 iterations to track progress
    if i % 2000 == 0:
        print(f"Iteration {i} - Error: {error:.6f} - Prediction: {final_output}")

print("\nFinal Prediction after 10,000 iterations:")
print(f"Output o1: {final_output[0]:.4f} (Target: 0.01)")
print(f"Output o2: {final_output[1]:.4f} (Target: 0.99)")