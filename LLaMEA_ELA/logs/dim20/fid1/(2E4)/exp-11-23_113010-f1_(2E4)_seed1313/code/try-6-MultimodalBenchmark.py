import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal terms with exponentially increasing frequencies
        sinusoidal_term = 0.0
        for i in range(1, min(6, self.dim + 1)):
            sinusoidal_term += np.sin(i * np.pi * x_normalized)**2 * np.exp(i)
        
        # High-order polynomial correlation term
        poly_correlation = np.sum(x_normalized**4) * np.prod(x_normalized)
        
        # Add a chaotic component using logistic map-like behavior
        chaotic_component = 0.0
        for i in range(self.dim):
            if i < len(x_normalized):
                chaotic_component += np.sin(100 * x_normalized[i] * np.cos(x_normalized[i]))
        
        # Combine all terms with varying weights to create a complex landscape
        return quadratic_term + 0.5 * sinusoidal_term + 0.05 * poly_correlation + 0.02 * chaotic_component