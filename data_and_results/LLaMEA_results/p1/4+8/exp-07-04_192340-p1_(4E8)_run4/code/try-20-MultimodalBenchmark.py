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
        f2 = np.sum(np.sin(12 * np.pi * x_normalized) ** 2)
        
        # Combined trigonometric term with varying frequencies
        f3 = np.sum(np.sin(4 * np.pi * x_normalized) * np.cos(8 * np.pi * x_normalized))
        
        # Exponential decay term to create plateaus
        f4 = np.sum(np.exp(-x_normalized**2) - 1.0)
        
        # Product of scaled dimensions for interaction effects
        f5 = np.prod(np.abs(x_normalized) + 0.15)
        
        # Add a chaotic shift to the global minimum
        shift = 0.2 * np.sum(np.sin(5 * x_normalized) * np.cos(5 * x_normalized))
        
        # Combine all terms with adaptive weights
        result = 0.25 * f1 + 0.45 * f2 + 0.1 * f3 + 0.1 * f4 + 0.1 * f5 + shift
        
        # Add structured noise for increased challenge
        noise = 0.01 * np.sum(np.sin(17 * x_normalized) * np.cos(17 * x_normalized))
        
        return result + noise