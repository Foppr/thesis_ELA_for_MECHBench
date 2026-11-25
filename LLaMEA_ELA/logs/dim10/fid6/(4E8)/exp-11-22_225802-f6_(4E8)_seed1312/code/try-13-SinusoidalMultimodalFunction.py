import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for sinusoidal behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Base sinusoidal components with multiple frequencies
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2 * scaled_x[i]) + \
                     0.5 * np.sin(3 * scaled_x[i]) * np.cos(4 * scaled_x[i])
            
        # Add quadratic penalty to encourage convergence to origin
        result += 0.1 * np.sum(x**2)
        
        # Add additional harmonic components for increased complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(5 * scaled_x[i]) * np.cos(6 * scaled_x[i])
            
        # Add periodic global minima pattern
        for i in range(self.dim):
            result += 0.2 * np.sin(0.5 * scaled_x[i]) * np.cos(0.7 * scaled_x[i])
            
        return result