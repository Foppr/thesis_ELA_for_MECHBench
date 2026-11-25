import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add sinusoidal perturbations to create multiple local minima
        f2 = 0.2 * np.sum(np.sin(5.0 * x + 0.5) * np.exp(-0.2 * x**2))
        
        # Add a global scaling factor to make the function more challenging
        f3 = 0.03 * np.sum(np.cos(10.0 * x - 0.3) * np.exp(-0.05 * x**2))
        
        # Add a small cubic term to increase landscape complexity
        f4 = 0.008 * np.sum(x**3)
        
        # Add a quartic term for additional landscape complexity
        f5 = 0.002 * np.sum(x**4)
        
        return f1 + f2 + f3 + f4 + f5