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
            grid_terms += np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            # Add additional grid structure with higher frequency components
            grid_terms += 0.3 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            # Include interaction terms between dimensions
            if i < self.dim - 1:
                grid_terms += 0.1 * np.sin(x[i]) * np.sin(x[i+1])
            # Add higher order nonlinear interactions
            grid_terms += 0.05 * np.sin(2.5 * x[i])**3 * np.cos(1.5 * x[i])
            # Add cross-dimension coupling with nonlinearity
            if i < self.dim - 2:
                grid_terms += 0.08 * np.sin(x[i] + x[i+1]) * np.cos(x[i+2])
        
        # Combine terms with different weights to create challenging landscape
        return basin + grid_terms + 0.02 * np.sum(np.abs(x)) + 0.005 * np.sum(x**4) + 0.01 * np.sum(np.sin(x)**2)