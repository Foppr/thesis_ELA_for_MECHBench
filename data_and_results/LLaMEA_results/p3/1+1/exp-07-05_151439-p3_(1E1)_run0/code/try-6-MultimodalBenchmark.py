import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Shifted global minimum to (1,1,...,1)
        x_shifted = x - 1.0
        
        # Base quadratic term
        term1 = np.sum(x_shifted**2) / self.dim
        
        # Cosine-based multimodal component with varying frequencies
        frequencies = np.arange(1, self.dim + 1)
        term2 = np.sum(np.cos(frequencies * np.pi * x_shifted / 2.0)) / self.dim
        
        # Product of cosines with different scaling factors
        term3 = np.prod(np.cos(x_shifted / (np.arange(1, self.dim + 1) * 0.3 + 0.5)))
        
        # Additional high-frequency oscillation component
        term4 = 0.15 * np.sum(np.sin(12 * x_shifted)) / self.dim
        
        # Add a sigmoidal modulation to create more complex valleys
        sigmoid_mod = np.prod(1.0 / (1.0 + np.exp(-x_shifted**2.5)))
        
        # Combine all terms with different weights
        result = term1 + term2 + term3 + term4 + 0.015 * sigmoid_mod
        
        return result