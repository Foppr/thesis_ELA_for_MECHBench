import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for sinusoidal behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Compute the function value with multiple sinusoidal components
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2 * scaled_x[i])
            
        # Add quadratic penalty to encourage convergence to origin
        result += 0.1 * np.sum(x**2)
        
        # Add multiple global minima at non-zero locations
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * scaled_x[i]) * np.cos(4 * scaled_x[i])
            
        return result