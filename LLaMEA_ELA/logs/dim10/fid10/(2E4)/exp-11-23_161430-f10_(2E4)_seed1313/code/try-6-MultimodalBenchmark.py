import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_sum = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1) * np.pi
        sin_sum = np.sum(np.sin(freqs * x_normalized)**2)
        
        # Add a Gaussian-like term to create more complex landscape
        gaussian_term = np.sum(np.exp(-x_normalized**2))
        
        # Introduce a mixed polynomial term for additional complexity
        mixed_term = np.sum(x_normalized**4 + 0.5 * x_normalized**6)
        
        # Combine all terms with adaptive weights based on dimensionality
        weight1 = 1.0
        weight2 = 0.3 / (1.0 + np.log(self.dim))
        weight3 = 0.05 / (1.0 + np.sqrt(self.dim))
        weight4 = 0.1 / (1.0 + self.dim**0.5)
        
        result = weight1 * quadratic_sum + weight2 * sin_sum + weight3 * gaussian_term + weight4 * mixed_term
        
        return result