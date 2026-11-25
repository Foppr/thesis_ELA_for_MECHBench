import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with shifted phase to create more complex landscape
        f2 = np.sum(np.sin(5 * np.pi * (x_norm + 0.1)) ** 2)
        
        # Product term with modified frequency to increase dimension interaction
        f3 = np.prod(np.cos(0.7 * np.pi * x_norm))
        
        # Additional cubic term for increased nonlinearity
        f4 = np.sum(x_norm**3)
        
        # Add a highly multimodal Gaussian radial component with multiple peaks
        gaussian_term = 0.0
        for i in range(self.dim):
            gaussian_term += np.exp(-np.sum((x_norm - np.sin(np.pi * (i + 1) / self.dim))**2) / (2 * 0.1**2))
        
        # Add a quartic polynomial term to increase landscape complexity
        f5 = np.sum(x_norm**4)
        
        # Combine all terms with different weights
        result = 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * gaussian_term + 0.05 * f5
        
        return result