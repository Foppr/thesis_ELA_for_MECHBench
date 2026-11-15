import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Additional high-frequency sinusoidal component for increased complexity
        high_freq = np.sum(np.sin(10 * np.pi * x_norm**2)**2)
        
        # Product of all dimensions (creates correlations)
        product = np.prod(x_norm)
        
        # Fourth-order polynomial term for additional landscape complexity
        quartic = np.sum(x_norm**4)
        
        # Add a small noise term to make it non-trivial
        noise = 0.05 * np.random.random()
        
        return quadratic + 0.5 * sinusoidal + 0.3 * high_freq + 0.1 * product + 0.2 * quartic + noise