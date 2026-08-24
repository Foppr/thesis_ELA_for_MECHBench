import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal phases for multi-scale oscillation
        self.phases = np.linspace(0, 2 * np.pi, dim, endpoint=False)
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.1, 0.5, dim)
        # Precompute polynomial chaos coefficients
        self.poly_chaos = np.random.normal(0, 1, (dim, 4))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-scale sinusoidal oscillation component
        sin_comp = np.sum(np.sin(self.phases * x_norm) * np.cos(3 * self.phases * x_norm))
        
        # Radial basis function component with dynamic widths
        rbf_comp = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.rbf_centers[i])**2)
            rbf_comp += np.exp(-dist / (2 * self.rbf_widths[i]**2))
        
        # Polynomial chaos expansion component
        poly_comp = 0.0
        for i in range(self.dim):
            x_i = x_norm[i]
            poly_comp += (self.poly_chaos[i, 0] + 
                         self.poly_chaos[i, 1] * x_i + 
                         self.poly_chaos[i, 2] * x_i**2 + 
                         self.poly_chaos[i, 3] * x_i**3)
        
        # Non-separable interaction term using cross-products
        cross_term = np.sum(x_norm**2) * np.sum(np.outer(x_norm, x_norm))
        
        # Sharp fitness transition using hyperbolic tangent
        transition = np.sum(np.tanh(10 * (x_norm - 0.5))**2)
        
        # Combine components with dynamic weights
        total = 0.25 * sin_comp + 0.3 * rbf_comp + 0.2 * poly_comp + 0.15 * cross_term + 0.1 * transition
        
        # Add global conditioning factor
        conditioning = 1.0 + 0.5 * np.sin(np.sum(x_norm**2) / self.dim)
        
        return total * conditioning