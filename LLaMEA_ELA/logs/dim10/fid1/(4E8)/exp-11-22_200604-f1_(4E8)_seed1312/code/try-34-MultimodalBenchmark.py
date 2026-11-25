import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different coefficients
        f1 = np.sum(x_norm**2)
        
        # Add multiple local minima using sinusoidal terms with higher frequency
        f2 = 0.3 * np.sum(np.sin(10 * np.pi * x_norm))
        
        # Add a quartic penalty term to create deeper valleys
        f3 = 0.05 * np.sum(x_norm**4)
        
        # Add an additional cubic term to increase complexity
        f4 = 0.08 * np.sum(x_norm**3)
        
        # Add a secondary trigonometric component with different frequency and amplitude
        f5 = 0.15 * np.sum(np.cos(7 * np.pi * x_norm**2))
        
        # Add a cross-term interaction to increase dimensionality complexity
        f6 = 0.03 * np.sum(x_norm[:-1] * x_norm[1:] * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6
        
        return result