import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal terms with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(12 * np.pi * x_normalized) + 0.5 * np.sin(24 * np.pi * x_normalized))
        
        # Additional cubic terms to increase landscape complexity
        f3 = 0.15 * np.sum(x_normalized**3)
        
        # Radial component with multiple peaks to create more challenging landscape
        radius = np.sqrt(np.sum(x_normalized**2))
        f4 = 0.2 * np.sin(10 * radius) * np.exp(-0.5 * radius**2)
        
        # Cross-dimensional interaction terms with higher-order polynomials
        f5 = 0.1 * np.sum((x_normalized[:-1] + x_normalized[1:])**4)
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5