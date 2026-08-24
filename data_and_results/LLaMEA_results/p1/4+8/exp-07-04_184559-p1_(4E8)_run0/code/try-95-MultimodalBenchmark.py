import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays and cosine modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-3 * r**2) * np.cos(5 * np.pi * r) * np.sin(2 * np.pi * r))
        
        # Coupled sinusoidal spiral terms for rotational complexity in all dimensions
        spiral = 0.0
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                if i + 1 < self.dim:
                    xi_norm = x_norm[i]
                    yi_norm = x_norm[i + 1]
                    theta = np.arctan2(yi_norm, xi_norm)
                    spiral += np.sin(6 * theta) * np.cos(5 * theta) * np.exp(-0.5 * (xi_norm**2 + yi_norm**2))
        
        # High-frequency oscillation with adaptive scaling based on dimensionality
        oscillation = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * (1 + 0.1 * np.abs(x_norm)))
        
        # Adaptive quadratic penalty with dimensionality-dependent scaling
        penalty = 0.3 * np.sum(x_norm**2) * (1 + 0.2 * np.log(self.dim + 1))
        
        # Additional interaction term between dimensions to increase complexity
        interaction = 0.1 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2)
        
        # Combine all components
        return radial + 2 * spiral + oscillation + penalty + interaction