import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Enhanced quadratic basin term with variable coefficients
        basin = 0.2 * np.sum(x**2) + 0.05 * np.sum(x**4)
        
        # Enhanced multimodal grid terms with higher frequency interactions
        grid_terms = 0
        for i in range(self.dim):
            # Multiple sine-cosine combinations creating complex landscape
            grid_terms += np.sin(1.0 * x[i]) * np.cos(0.7 * x[i])
            grid_terms += 0.3 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i])
            grid_terms += 0.2 * np.sin(3.0 * x[i]) * np.cos(2.2 * x[i])
            # Add periodic grid structure with varying amplitudes
            grid_terms += 0.1 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Additional coupling terms between dimensions to increase complexity
        coupling = 0
        for i in range(self.dim-1):
            coupling += 0.1 * np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        
        # Combine all terms with different weights
        return basin + grid_terms + coupling + 0.02 * np.sum(np.abs(x)) + 0.005 * np.sum(x**6)