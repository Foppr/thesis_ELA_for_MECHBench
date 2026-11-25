import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with asymmetric penalty
        r = np.sqrt(np.sum(x_norm**2))
        radial = r * (1 + 0.3 * np.sin(2 * np.pi * r) + 0.2 * np.cos(4 * np.pi * r))
        
        # Periodic lattice structure in all dimensions with enhanced frequency
        periodic = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms with higher-order coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i] - x_norm[j])**3 * np.sin(x_norm[i] + x_norm[j])
        
        # Asymmetric quadratic terms with different weights for positive/negative values
        asym_quad = np.sum(np.where(x_norm > 0, 0.8 * x_norm**2, 1.2 * x_norm**2))
        
        # Additional multimodal component with multiple local minima
        multimodal = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Add a global scaling factor and noise
        noise = 0.005 * np.random.random()
        
        return 1.5 * radial + 0.6 * periodic + 0.4 * cross_term + asym_quad + 0.3 * multimodal + noise