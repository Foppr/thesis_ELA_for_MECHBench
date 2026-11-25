import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add sinusoidal perturbations with higher frequency and different amplitude
        f2 = 0.2 * np.sum(np.sin(10.0 * x))
        
        # Add a cubic term to increase function curvature
        f3 = 0.05 * np.sum(x**3)
        
        # Add a quartic term to increase function curvature
        f4 = 0.01 * np.sum(x**4)
        
        # Combine terms with different weights to create challenging landscape
        return f1 + f2 + f3 + f4