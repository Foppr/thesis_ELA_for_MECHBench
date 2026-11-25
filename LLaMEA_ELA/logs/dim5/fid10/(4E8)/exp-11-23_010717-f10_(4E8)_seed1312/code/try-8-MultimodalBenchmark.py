import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic_term = np.sum(x_normalized**2)
        
        # High-frequency sine waves creating dense local minima
        sine_term = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized))
        
        # Exponentially scaled cosine terms for nested structure
        cos_term = np.sum(np.exp(-np.abs(x_normalized)) * np.cos(3 * np.pi * x_normalized))
        
        # Logarithmic scaling to create chaotic behavior near boundaries
        log_term = np.sum(np.log(1 + np.abs(x_normalized)) * np.sin(2 * np.pi * x_normalized))
        
        # Polynomial interaction term for complex dimension coupling
        poly_term = np.prod(np.sin(0.5 * np.pi * x_normalized) + 0.5)
        
        # Combine all terms with varying weights to create a challenging landscape
        result = 0.2 * quadratic_term - 0.8 * sine_term + 0.4 * cos_term + 0.3 * log_term + 0.1 * poly_term
        
        return result