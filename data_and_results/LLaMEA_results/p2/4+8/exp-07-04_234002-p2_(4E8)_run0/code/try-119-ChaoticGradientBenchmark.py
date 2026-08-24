import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial base with varying degrees
        for i in range(self.dim):
            result += 0.5 * x[i]**2 + 0.1 * x[i]**4 + 0.02 * x[i]**6
            
        # Exponential coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) + 0.3 * np.exp(-0.05 * (x[i] + x[j])**2)
                result += 0.2 * coupling * (x[i]**2 + x[j]**2)
                
        # Chaotic gradient component using sine and cosine with varying frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) + 0.1 * np.sin(15.0 * x[i]**2)
            
        # Adaptive scaling factor based on dimensionality and position
        scaling = 1.0 + 0.5 * np.sum(np.abs(x)) / self.dim + 0.2 * np.sum(x**2) / self.dim
        
        # Add a fractal-like perturbation using recursive sine components
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += 0.05 * np.sin(20.0 * x[i]) * np.sin(30.0 * x[i]) * np.sin(40.0 * x[i])
            
        result = result * scaling + fractal_perturbation
        
        return result