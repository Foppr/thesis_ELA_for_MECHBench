import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_normalized) ** 2)
        
        # Combined trigonometric term with varying frequencies
        f3 = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized))
        
        # Exponential decay term to create plateaus
        f4 = np.sum(np.exp(-x_normalized**2) - 1.0)
        
        # Product of scaled dimensions for interaction effects
        f5 = np.prod(np.abs(x_normalized) + 0.1)
        
        # Combine all terms with adaptive weights
        result = 0.3 * f1 + 0.4 * f2 + 0.1 * f3 + 0.1 * f4 + 0.1 * f5
        
        # Add structured noise for increased challenge
        noise = 0.02 * np.sum(np.sin(15 * x_normalized) * np.cos(15 * x_normalized))
        
        return result + noise