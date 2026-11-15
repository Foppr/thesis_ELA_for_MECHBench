import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Product of sinusoidal terms with higher frequency to create more local minima
        sinusoidal = np.prod(np.sin(7 * np.pi * x_norm))
        
        # Add a penalty term for large values to encourage convergence to origin
        penalty = 0.15 * np.sum(x_norm**4)
        
        # Add a cross-term interaction to increase landscape complexity
        cross_term = 0.05 * np.sum(x_norm**3) * np.sum(np.sin(np.pi * x_norm))
        
        # Combine terms to create a challenging landscape
        return quadratic + 15 * sinusoidal + penalty + cross_term