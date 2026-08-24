import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**4)
        
        # Add hyperbolic tangent components for smooth but steep transitions
        for i in range(self.dim):
            f_val += 0.5 * np.tanh(2 * x[i])**2 + 0.3 * np.tanh(0.5 * x[i]) * np.sin(3 * x[i])
        
        # Add cross-variable interactions with hyperbolic sine
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sinh(0.5 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
        
        # Add polynomial terms modulated by sine functions
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**6) * np.sin(4 * x[i]) + 0.03 * (x[i]**4) * np.cos(x[i])
        
        # Add a global sinusoidal modulation based on the sum of variables
        f_val += 0.2 * np.sin(0.3 * np.sum(x)) * np.cos(0.2 * np.sum(x**2))
        
        # Add local minima using Gaussian-like peaks with varying heights
        for i in range(self.dim):
            f_val += 0.1 * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(5 * (x[i] + 2.0))
        
        # Add a penalty term for distance from the origin to encourage convergence
        f_val += 0.02 * np.sum(x**2) * (1 + 0.1 * np.sin(10 * np.sum(x**2)))
        
        return f_val