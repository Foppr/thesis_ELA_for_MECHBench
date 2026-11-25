import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sinusoidal components with increased frequency modulation
        f2 = 0.7 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm))
        
        # Stronger higher-order polynomial terms with altered weights for increased landscape complexity
        f3 = 0.25 * np.sum(x_norm**8)
        
        # Modified cross-terms with enhanced non-linear coupling
        f4 = 0.35 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * x_norm**4)
        
        # Additional polynomial cross-terms with varying exponents and modified coefficients
        f5 = 0.12 * np.sum(x_norm**5 * np.sin(7 * np.pi * x_norm))
        
        # Shifted and modulated sinusoidal component with altered parameters to create additional local optima
        f6 = 0.35 * np.sum(np.sin(6 * np.pi * (x_norm + 0.2)) * np.cos(8 * np.pi * (x_norm - 0.2)) * np.tan(4 * np.pi * x_norm))
        
        # New quintic cross-term with modified frequency modulation
        f7 = 0.18 * np.sum(x_norm**5 * np.cos(4 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Non-linear interaction term with adjusted weights for enhanced complexity
        f8 = 0.25 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * (x_norm**3 + 0.15))
        
        # Additional chaotic component with exponential modulation
        f9 = 0.2 * np.sum(np.exp(2 * x_norm) * np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm))
        
        # Combined result with modified weights for increased multimodality
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
        
        return result