import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply random noise injection to create more challenging landscape
        noise = np.random.normal(0, 0.1, self.dim)
        
        # Shift variables to center the function with random offset
        shifted_x = x - (1.0 + noise)
        
        # Compute multiple sinusoidal components with exponentially increasing frequencies
        term1 = np.sum(shifted_x**2) / self.dim
        term2 = np.sum(np.cos(2 * np.pi * shifted_x * 2**(np.arange(self.dim) + 1))) / self.dim
        term3 = np.sum(shifted_x**4) / (4 * self.dim)
        
        # Add exponential decay term to create complex landscape
        term4 = np.sum(np.exp(-shifted_x**2 / 2)) / self.dim
        
        # Add polynomial basin with random coefficients
        poly_coeffs = np.random.uniform(0.1, 0.5, self.dim)
        term5 = np.sum(poly_coeffs * shifted_x**6) / (6 * self.dim)
        
        # Combine all terms with varying weights
        result = 0.5 * term1 + 0.3 * term2 + 0.2 * term3 + 0.1 * term4 + 0.1 * term5
        
        return float(result)