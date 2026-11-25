import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal grid terms - multiple global minima arranged in a grid
        grid_terms = 0
        for i in range(self.dim):
            # Create periodic pattern with multiple local minima
            grid_terms += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            # Add additional grid structure
            grid_terms += 0.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Combine terms with different weights to create challenging landscape
        return basin + grid_terms + 0.01 * np.sum(np.abs(x))