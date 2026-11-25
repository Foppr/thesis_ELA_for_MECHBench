import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic term with adaptive scaling based on dimensionality
        quadratic_term = np.sum(x_normalized**2) * (1.0 + 0.1 * self.dim)
        
        # Multiple sine waves with different frequencies to create complex landscape
        sine_term = np.sum(np.sin(3 * np.pi * x_normalized) + 0.5 * np.sin(7 * np.pi * x_normalized))
        
        # Cosine product term with varying phase shifts for increased complexity
        cos_product = np.prod(np.cos(0.3 * np.pi * x_normalized + 0.1 * np.arange(self.dim)))
        
        # Additional Gaussian-like peaks to introduce multiple shallow minima
        gaussian_peaks = np.sum(np.exp(-2.0 * (x_normalized**2)) * np.cos(4 * np.pi * x_normalized))
        
        # Combine all terms with carefully tuned weights
        result = 0.2 * quadratic_term - 0.8 * sine_term + 0.4 * cos_product - 0.3 * gaussian_peaks
        
        return result