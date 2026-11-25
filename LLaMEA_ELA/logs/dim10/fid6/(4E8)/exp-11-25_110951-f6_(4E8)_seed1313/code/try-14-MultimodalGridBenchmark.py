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
            # Add additional grid structure with higher frequency components
            grid_terms += 0.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            # Add even higher frequency for sharper landscape
            grid_terms += 0.3 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Add a small noise-like term to increase complexity
        noise = 0.05 * np.sum(np.sin(x) * np.cos(0.1 * x))
        
        # Combine terms with different weights to create challenging landscape
        return basin + grid_terms + noise + 0.01 * np.sum(np.abs(x))