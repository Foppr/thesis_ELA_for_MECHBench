import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Multiple sinusoidal perturbations with different frequencies
        f2 = 0.5 * np.sum(np.sin(10.0 * x) + 0.5 * np.sin(20.0 * x))
        
        # Add a more complex polynomial term to increase landscape complexity
        f3 = 0.01 * np.sum(x**4)
        
        # Add a cosine term to create additional local optima
        f4 = 0.3 * np.sum(np.cos(5.0 * x))
        
        # Combine all terms with different weights
        result = f1 + f2 + f3 + f4
        
        return result