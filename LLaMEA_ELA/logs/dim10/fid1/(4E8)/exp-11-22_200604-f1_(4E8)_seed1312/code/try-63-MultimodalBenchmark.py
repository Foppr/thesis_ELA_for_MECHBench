import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with frequency modulation
        f2 = 0.8 * np.sum(np.sin(12 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm))
        
        # Add higher-order polynomial terms for increased landscape complexity
        f3 = 0.15 * np.sum(x_norm**8)
        
        # Introduce cross-terms with non-linear coupling
        f4 = 0.25 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * x_norm**4)
        
        # Additional polynomial cross-terms with varying exponents
        f5 = 0.08 * np.sum(x_norm**5 * np.sin(9 * np.pi * x_norm))
        
        # Shifted and modulated sinusoidal component to create additional local optima
        f6 = 0.35 * np.sum(np.sin(8 * np.pi * (x_norm + 0.15)) * np.cos(10 * np.pi * (x_norm - 0.15)) * np.tan(3 * np.pi * x_norm))
        
        # New cubic cross-term with frequency modulation
        f7 = 0.12 * np.sum(x_norm**4 * np.cos(5 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm))
        
        # Non-linear interaction term for enhanced complexity
        f8 = 0.18 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * (x_norm**2 + 0.15))
        
        # Additional chaotic component with exponential weighting
        f9 = 0.2 * np.sum(np.exp(-x_norm**2) * np.sin(10 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm))
        
        # Cross-dimensional coupling with sine modulation
        f10 = 0.1 * np.sum(np.sin(np.pi * np.sum(x_norm**2)) * x_norm**6)
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result