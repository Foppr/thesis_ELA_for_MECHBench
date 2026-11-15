import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal phases for multi-scale oscillation
        self.phases = np.linspace(0, 2 * np.pi, dim, endpoint=False)
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.widths = np.random.uniform(0.5, 2.0, dim)
        # Precompute polynomial weights for global scaling
        self.poly_weights = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-scale sinusoidal oscillation component
        sin_comp = np.sum(np.sin(self.phases * x_norm) * np.cos(2 * self.phases * x_norm))
        
        # Radial basis function component with varying widths
        rbf_comp = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            rbf_comp += np.exp(-dist / (2 * self.widths[i]**2))
        
        # Polynomial interaction with global weights
        poly_comp = np.sum(self.poly_weights * (x_norm**3 + 0.5 * x_norm**5))
        
        # Cross-dimensional interaction term
        cross_term = np.sum(np.sin(x_norm[:-1] - x_norm[1:]))
        
        # Global conditioning penalty
        cond_penalty = 0.1 * np.sum(x_norm**2) * (1 + 0.2 * np.sin(np.sum(x_norm)))
        
        # Combine all components
        total = 0.3 * sin_comp + 0.4 * rbf_comp + 0.2 * poly_comp + 0.05 * cross_term + 0.05 * cond_penalty
        
        return total