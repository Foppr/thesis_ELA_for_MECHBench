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
        f2 = 0.3 * np.sum(np.sin(6.0 * x + 0.7) * np.exp(-0.15 * x**2))
        
        # Add a global scaling factor to make the function more challenging
        f3 = 0.04 * np.sum(np.cos(12.0 * x - 0.4) * np.exp(-0.03 * x**2))
        
        # Add a small cubic term to increase landscape complexity
        f4 = 0.01 * np.sum(x**3)
        
        # Add a quartic term for additional landscape complexity
        f5 = 0.005 * np.sum(x**4)
        
        # Add chaotic sine modulation for increased ruggedness
        f6 = 0.02 * np.sum(np.sin(15.0 * x + np.sin(x)) * np.exp(-0.1 * x**2))
        
        # Add quartic interaction term between dimensions
        f7 = 0.003 * np.sum((x[None, :] - x[:, None])**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7