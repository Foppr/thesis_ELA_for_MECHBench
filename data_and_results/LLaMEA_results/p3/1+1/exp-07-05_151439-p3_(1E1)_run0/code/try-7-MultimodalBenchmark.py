import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with increased complexity
        # Global minimum at origin (0,0,...,0) with value 0
        # Multiple local minima with varying depths and distances
        
        # Base quadratic term
        term1 = np.sum(x**2) / self.dim
        
        # Cosine-based multimodal component with varying frequencies
        frequencies = np.arange(1, self.dim + 1)
        term2 = np.sum(np.cos(frequencies * np.pi * x / 2.5)) / self.dim
        
        # Product of cosines with different scaling factors
        term3 = np.prod(np.cos(x / (np.arange(1, self.dim + 1) * 0.5 + 1.0)))
        
        # Additional high-frequency oscillation component
        term4 = 0.1 * np.sum(np.sin(10 * x)) / self.dim
        
        # Add a sigmoidal modulation to create more complex valleys
        sigmoid_mod = np.prod(1.0 / (1.0 + np.exp(-x**2)))
        
        # Combine all terms with different weights
        result = term1 + term2 + term3 + term4 + 0.01 * sigmoid_mod
        
        return result