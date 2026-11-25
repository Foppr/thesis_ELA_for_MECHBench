import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal terms with exponentially increasing frequencies to create dense local optima
        f2 = 0.0
        for i in range(1, self.dim + 1):
            f2 += np.sin(i * np.pi * x_norm) ** 2
        
        # Higher-order polynomial terms (quartic and quintic) for increased nonlinearity
        f3 = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**5)
        
        # Cross-dimensional interaction through product of cosines with varying scales
        f4 = 1.0
        for i in range(self.dim):
            f4 *= np.cos((i + 1) * 0.5 * np.pi * x_norm[i])
        
        # Additional noise-like term using Gaussian random components to increase ruggedness
        noise = np.random.normal(0, 0.01, self.dim)
        f5 = np.sum(noise * x_norm)
        
        # Combine all terms with carefully tuned weights
        return f1 + 0.3 * f2 + 0.1 * f3 - 0.05 * f4 + 0.02 * f5