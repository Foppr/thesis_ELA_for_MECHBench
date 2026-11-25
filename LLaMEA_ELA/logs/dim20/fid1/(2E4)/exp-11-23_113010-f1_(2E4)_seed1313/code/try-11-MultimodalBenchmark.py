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
        radial = r * (1 + 0.5 * np.sin(3 * np.pi * r))
        
        # Periodic lattice structure in all dimensions
        periodic = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i] - x_norm[j])**2 * np.sin(x_norm[i] + x_norm[j])
        
        # Asymmetric quadratic terms
        asym_quad = np.sum(np.where(x_norm > 0, x_norm**2, 0.5 * x_norm**2))
        
        # Add a global scaling factor and noise
        noise = 0.01 * np.random.random()
        
        return 2 * radial + 0.8 * periodic + 0.3 * cross_term + asym_quad + noise