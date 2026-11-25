import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima and chaotic modulation
        f2 = np.sum(np.sin(12 * np.pi * x_norm * (1 + 0.3 * np.sin(7 * x_norm)))**2)
        
        # Product term creating complex landscape with chaotic perturbation
        f3 = np.prod(np.cos(1.2 * np.pi * x_norm * (1 + 0.2 * np.sin(5 * x_norm))) + 0.2)
        
        # Additional polynomial interaction term with cubic power and cross-terms
        f4 = np.sum(x_norm**3 + 0.1 * np.prod(x_norm.reshape(-1, 1) - x_norm.reshape(1, -1), axis=1))
        
        # Shifted global minimum term with sinusoidal perturbation
        f5 = np.sum((x_norm + 0.2 * np.sin(3 * x_norm))**2)
        
        # Additional quartic polynomial term for increased complexity
        f6 = np.sum(x_norm**4)
        
        # Higher-order polynomial term to increase complexity with chaotic modulation
        f7 = np.sum(x_norm**5 * (1 + 0.1 * np.sin(8 * x_norm)))
        
        # Additional sinusoidal component with different frequency and chaotic modulation
        f8 = np.sum(np.sin(7 * np.pi * x_norm**2 * (1 + 0.2 * np.cos(4 * x_norm)))**2)
        
        # Cross-term interaction between all dimensions
        f9 = np.sum((x_norm.reshape(-1, 1) - x_norm.reshape(1, -1))**2 * np.exp(-0.5 * np.sum((x_norm.reshape(-1, 1) - x_norm.reshape(1, -1))**2, axis=1)))
        
        # Combined with different weights to create a more challenging landscape
        return 0.1 * f1 + 0.3 * f2 + 0.15 * f3 + 0.1 * f4 + 0.15 * f5 + 0.1 * f6 + 0.05 * f7 + 0.1 * f8 + 0.05 * f9 + 1.5