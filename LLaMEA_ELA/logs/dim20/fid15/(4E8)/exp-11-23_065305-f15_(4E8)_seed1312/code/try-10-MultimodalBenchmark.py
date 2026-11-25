import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply rotation and scaling for increased complexity
        scaled_x = x * 0.5
        
        # Compute multiple sinusoidal components with different frequencies
        term1 = np.sum(scaled_x**2) / self.dim
        term2 = np.sum(np.cos(2 * np.pi * scaled_x)) / self.dim
        term3 = np.sum(np.sin(3 * np.pi * scaled_x)) / self.dim
        
        # Add higher-order polynomial terms for increased landscape complexity
        term4 = np.sum(scaled_x**6) / (6 * self.dim)
        
        # Add a multi-modal component with multiple global minima
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.sin(5 * np.pi * scaled_x[i]) * np.cos(2 * np.pi * scaled_x[i])
        
        result = term1 - term2 + term3 + term4 + 0.1 * multi_modal
        
        return float(result)