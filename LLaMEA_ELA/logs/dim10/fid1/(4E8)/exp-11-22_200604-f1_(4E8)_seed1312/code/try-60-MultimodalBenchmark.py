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
        f2 = 0.6 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Add higher-order polynomial terms for increased landscape complexity
        f3 = 0.12 * np.sum(x_norm**7)
        
        # Introduce cross-terms with non-linear coupling
        f4 = 0.2 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * x_norm**3)
        
        # Additional polynomial cross-terms with varying exponents
        f5 = 0.05 * np.sum(x_norm**4 * np.sin(7 * np.pi * x_norm))
        
        # Shifted and modulated sinusoidal component to create additional local optima
        f6 = 0.3 * np.sum(np.sin(6 * np.pi * (x_norm + 0.2)) * np.cos(8 * np.pi * (x_norm - 0.2)) * np.tan(2 * np.pi * x_norm))
        
        # New cubic cross-term with frequency modulation
        f7 = 0.1 * np.sum(x_norm**3 * np.cos(4 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm))
        
        # Non-linear interaction term for enhanced complexity
        f8 = 0.15 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * (x_norm**2 + 0.1))
        
        # Add a new chaotic component with exponential modulation and additional sinusoidal layers
        f9 = 0.25 * np.sum(np.exp(3 * x_norm) * np.sin(12 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Introduce a complex polynomial interaction with trigonometric modulation and dynamic exponents
        f10 = 0.18 * np.sum((x_norm**5 + x_norm**3) * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Add a new hyperbolic component to increase the number of local minima
        f11 = 0.22 * np.sum(np.sinh(2 * x_norm) * np.cos(8 * np.pi * x_norm) * x_norm**2)
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        
        return result