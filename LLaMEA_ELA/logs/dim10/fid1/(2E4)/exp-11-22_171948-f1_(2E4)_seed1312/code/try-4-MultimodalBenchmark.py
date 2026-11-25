import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base with conditioning
        quadratic_sum = np.sum(x_normalized**2)
        
        # Exponentially increasing sinusoidal terms for more complex landscape
        sinusoidal_term = 0
        for i in range(1, min(6, self.dim + 1)):
            sinusoidal_term += np.sin(i * np.pi * x_normalized)**2 * np.exp(i)
        
        # Add saddle points with higher-order polynomial terms
        saddle_term = np.sum(x_normalized**4) - 0.5 * np.sum(x_normalized**2)
        
        # Combine all terms with different scaling factors
        result = quadratic_sum + 0.5 * sinusoidal_term + 0.1 * saddle_term
        
        return result