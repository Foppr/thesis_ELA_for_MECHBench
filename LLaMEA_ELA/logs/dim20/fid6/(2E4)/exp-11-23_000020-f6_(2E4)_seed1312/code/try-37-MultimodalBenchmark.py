import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-wave interference with varying frequencies
        f2 = np.sum(np.sin(11 * np.pi * x_norm + np.sin(7 * x_norm))**2)
        
        # Product term creating complex landscape with nonlinear coupling
        f3 = np.prod(np.cos(0.9 * np.pi * x_norm) + 0.2)
        
        # Additional polynomial interaction term with cubic power and shift
        f4 = np.sum((x_norm + 0.1)**3)
        
        # Shifted global minimum term with sinusoidal modulation
        f5 = np.sum((x_norm + 0.3)**2 * (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Additional quartic polynomial term for increased complexity
        f6 = np.sum(x_norm**4)
        
        # Higher-order polynomial term with exponential scaling
        f7 = np.sum(np.exp(0.5 * x_norm) * x_norm**3)
        
        # Additional sinusoidal component with multi-modal frequency modulation
        f8 = np.sum(np.sin(6 * np.pi * x_norm**2 + 0.5 * np.sin(4 * x_norm))**2)
        
        # Combined with different weights to create a more challenging landscape
        return 0.1 * f1 + 0.3 * f2 + 0.25 * f3 + 0.1 * f4 + 0.15 * f5 + 0.1 * f6 + 0.05 * f7 + 0.1 * f8 + 1.5