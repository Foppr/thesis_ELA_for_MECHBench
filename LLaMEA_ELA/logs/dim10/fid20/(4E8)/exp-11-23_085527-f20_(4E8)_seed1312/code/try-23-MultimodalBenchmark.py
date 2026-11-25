import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_normalized = x / 5.0
        
        # Quadratic term with varying coefficients for different dimensions
        f1 = np.sum((x_normalized**2) * np.arange(1, self.dim + 1))
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_normalized**3))
        
        # Asymmetric saddle point terms using cubic polynomials
        f3 = np.sum(x_normalized**3 * np.cos(2 * np.pi * x_normalized))
        
        # Interaction term with exponential decay to create complex valleys
        f4 = np.exp(-np.sum(x_normalized**2)) * np.sin(np.pi * np.sum(x_normalized))
        
        # Additional noise-like term using prime numbers for dimension indexing
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29][:self.dim]
        f5 = np.sum(np.sin(primes * x_normalized) / (primes + 1))
        
        # Combine all terms with varying weights
        return 0.5 * f1 + 2.0 * f2 + 0.3 * f3 + 0.1 * f4 + 0.8 * f5