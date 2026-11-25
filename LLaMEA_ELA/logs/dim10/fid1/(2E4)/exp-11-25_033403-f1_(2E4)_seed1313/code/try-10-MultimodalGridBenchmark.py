import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - encourages convergence to center
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal grid terms - create multiple local minima in a grid pattern
        grid_terms = 0.0
        for i in range(self.dim):
            # Create periodic structure with multiple minima
            grid_terms += np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            # Add higher frequency components for increased complexity
            grid_terms += 0.3 * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i])
            # Add cross-terms between dimensions for increased interaction
            if i > 0:
                grid_terms += 0.1 * np.sin(0.8 * x[i-1]) * np.cos(0.7 * x[i])
        
        # Combine terms with different weights to create challenging landscape
        return basin + 0.6 * grid_terms + 1.5 * np.sum(np.abs(x)) / self.dim