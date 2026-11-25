import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_normalized) ** 2)
        
        # Additional cosine terms to increase landscape complexity
        f3 = np.sum(np.cos(3 * np.pi * x_normalized) ** 2)
        
        # Polynomial term to create more complex valleys
        f4 = np.sum(x_normalized**4)
        
        # Combine all terms with different weights
        result = f1 + 0.5 * f2 + 0.3 * f3 + 0.1 * f4
        
        # Add small random perturbation to avoid deterministic behavior
        noise = 0.01 * np.random.random()
        
        return result + noise