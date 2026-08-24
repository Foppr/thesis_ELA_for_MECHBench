import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Fractal-like cosine pattern with self-similar structure
        f2 = np.sum(np.cos(2**(np.arange(1, self.dim + 1)) * np.pi * x_norm) ** 2)
        
        # Gradient-based attraction field with varying strengths
        f3 = np.sum((x_norm - np.sin(x_norm))**2)
        
        # Dynamic noise term that scales with dimensionality
        noise = np.random.normal(0, 0.01 * np.log(self.dim + 1), self.dim)
        f4 = np.sum((x_norm + noise)**4)
        
        # Multi-scale sinusoidal coupling with exponentially increasing frequencies
        freqs = np.logspace(0, 2, self.dim)
        f5 = np.sum(np.sin(freqs * x_norm) ** 2)
        
        # Cross-dimensional interaction with power-law scaling
        f6 = np.sum(np.abs(x_norm[:-1] * x_norm[1:]) ** (1.5 + np.arange(self.dim - 1)))
        
        # Dynamic scaling factor based on dimensionality
        scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all terms with dynamic weights
        return f1 + 0.5 * f2 + 0.3 * f3 + 0.2 * f4 + 0.4 * f5 + 0.1 * f6 * scale