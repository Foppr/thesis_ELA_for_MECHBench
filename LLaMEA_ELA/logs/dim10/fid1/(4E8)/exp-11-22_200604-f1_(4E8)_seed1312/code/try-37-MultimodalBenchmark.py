import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Add higher-order polynomial terms for increased landscape complexity
        f3 = 0.1 * np.sum(x_norm**6)
        
        # Introduce cross-terms to create more complex interaction patterns
        f4 = 0.2 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Additional polynomial cross-terms for enhanced complexity
        f5 = 0.05 * np.sum(x_norm**3 * np.sin(4 * np.pi * x_norm))
        
        # Shifted sinusoidal component to create additional local optima
        f6 = 0.25 * np.sum(np.sin(5 * np.pi * (x_norm + 0.1)) * np.cos(7 * np.pi * (x_norm - 0.1)))
        
        # New cubic cross-term to increase landscape complexity
        f7 = 0.1 * np.sum(x_norm**3 * np.cos(3 * np.pi * x_norm))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result