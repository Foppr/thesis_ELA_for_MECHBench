import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squared terms with different weights
        term1 = np.sum(x_norm**2)
        
        # Add multiple local minima using sinusoidal components with higher frequency
        term2 = 0.3 * np.sum(np.sin(9 * np.pi * x_norm))
        
        # Add a more complex multimodal component with different polynomial power
        term3 = 0.15 * np.sum((x_norm**7) * np.cos(4 * np.pi * x_norm))
        
        # Add interaction terms between dimensions with modified coupling
        term4 = 0.08 * np.sum(x_norm[:-1] * x_norm[1:] * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Shift global minimum to a non-zero point with perturbation
        shift = 0.15
        term5 = 0.12 * np.sum((x_norm - shift)**2)
        
        # Add cubic polynomial interaction for increased complexity
        term6 = 0.03 * np.sum(x_norm**3)
        
        # Combine terms with different scaling factors
        result = term1 + term2 + term3 + term4 + term5 + term6
        
        return result