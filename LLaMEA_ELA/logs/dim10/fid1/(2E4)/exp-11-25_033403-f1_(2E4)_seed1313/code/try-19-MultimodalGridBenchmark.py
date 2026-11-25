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
            grid_terms += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            # Add higher frequency components for increased complexity
            grid_terms += 0.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            # Add even higher frequency interactions for more complex landscape
            grid_terms += 0.3 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Add interaction terms between dimensions to increase complexity
        interaction_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_terms += 0.1 * np.sin(x[i]) * np.cos(x[j])
        
        # Combine terms with different weights to create challenging landscape
        return basin + 0.5 * grid_terms + 0.3 * interaction_terms + 2.0 * np.sum(np.abs(x)) / self.dim