import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term with modified weight for global attraction
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Multiple high-frequency sinusoidal components with varying amplitudes
        f2 = 0.4 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Add higher-order polynomial terms with different exponents for increased complexity
        f3 = 0.1 * np.sum(x_norm**8)
        
        # Introduce cross-terms with trigonometric interactions to create complex valleys
        f4 = 0.2 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                         np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Add a quartic polynomial component to increase landscape ruggedness
        f5 = 0.05 * np.sum((x_norm**2 - 1)**2)
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5
        
        return result