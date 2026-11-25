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
            grid_terms += np.sin(0.5 * x[i] + 1.0) * np.cos(0.3 * x[i] + 0.5)
            # Add higher frequency components for increased complexity
            grid_terms += 0.5 * np.sin(2.0 * x[i] + 0.2) * np.cos(1.5 * x[i] + 0.8)
            # Add interaction terms between dimensions
            if i < self.dim - 1:
                grid_terms += 0.3 * np.sin(0.4 * (x[i] + x[i+1])) * np.cos(0.6 * (x[i] - x[i+1]))
        
        # Combine terms with different weights to create challenging landscape
        return basin + 0.5 * grid_terms + 2.0 * np.sum(np.abs(x)) / self.dim