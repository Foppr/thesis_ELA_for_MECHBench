import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for sinusoidal behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Base sinusoidal component with multiple frequencies
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2 * scaled_x[i]) + 0.3 * np.sin(3 * scaled_x[i])
            
        # Add quadratic penalty to encourage convergence to origin
        result += 0.1 * np.sum(x**2)
        
        # Add multiple global minima at non-zero locations with varying amplitudes
        for i in range(self.dim):
            result += 0.4 * np.sin(4 * scaled_x[i]) * np.cos(5 * scaled_x[i]) + 0.2 * np.sin(6 * scaled_x[i])
            
        # Add a central valley to guide optimization algorithms
        result -= 0.3 * np.exp(-0.1 * np.sum(x**2))
        
        return result