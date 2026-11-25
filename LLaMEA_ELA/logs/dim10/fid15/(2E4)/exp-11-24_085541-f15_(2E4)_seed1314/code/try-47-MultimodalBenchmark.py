import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponential decay with sinusoidal modulation
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.5 * x[i]**2) * np.sin(3.0 * x[i])
            
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.5 * np.cos(x[i] + x[j]) * np.sin(0.5 * x[i] * x[j])
                
        # Add fractal-like recursive component with diminishing weights
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, 10):
                recursive_sum += (0.3**k) * np.sin((2**k) * x[i])
            result += recursive_sum
            
        # Add multi-modal component with polynomial and exponential interactions
        for i in range(self.dim):
            result += 0.7 * x[i]**4 - 1.2 * x[i]**3 + 0.8 * x[i]**2 - 0.4 * x[i] + 0.1 * np.exp(-x[i]**2)
            
        # Add chaotic sine waves with varying frequencies
        for i in range(self.dim):
            result += 1.2 * np.sin(7.0 * x[i]) * np.cos(5.0 * x[i]) * np.sin(3.0 * x[i])
            
        # Add cross-dimensional polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**2 + x[j]**2) * (x[i] * x[j])**0.5
        result += 0.6 * poly_coupling
        
        # Add conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.3 * self.dim
        result *= condition_factor
        
        # Add penalty for exceeding bounds with exponential scaling
        bound_penalty = np.sum(np.exp(np.abs(x) - 5.0))
        result += 0.8 * bound_penalty
        
        return result