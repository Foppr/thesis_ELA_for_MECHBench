import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with modified frequency modulation
        f2 = 0.5 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm))
        
        # Add higher-order polynomial terms with altered weights for increased landscape complexity
        f3 = 0.15 * np.sum(x_norm**7)
        
        # Introduce cross-terms with modified non-linear coupling
        f4 = 0.25 * np.sum(np.sin(6 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * x_norm**3)
        
        # Additional polynomial cross-terms with varying exponents and modified coefficients
        f5 = 0.07 * np.sum(x_norm**4 * np.sin(6 * np.pi * x_norm))
        
        # Shifted and modulated sinusoidal component with altered parameters to create additional local optima
        f6 = 0.25 * np.sum(np.sin(5 * np.pi * (x_norm + 0.18)) * np.cos(7 * np.pi * (x_norm - 0.12)) * np.tan(3 * np.pi * x_norm))
        
        # New cubic cross-term with modified frequency modulation
        f7 = 0.12 * np.sum(x_norm**3 * np.cos(3 * np.pi * x_norm) * np.sin(6.5 * np.pi * x_norm))
        
        # Non-linear interaction term with adjusted weights for enhanced complexity
        f8 = 0.18 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * (x_norm**2 + 0.15))
        
        # Add a small perturbation to the fifth term to increase variability
        f9 = 0.05 * np.sum(x_norm**5 * np.cos(4 * np.pi * x_norm))
        
        # Introduce a new quartic cross-term with modified coefficients for additional complexity
        f10 = 0.1 * np.sum(x_norm**4 * np.sin(5 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Combine all components with slightly different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result