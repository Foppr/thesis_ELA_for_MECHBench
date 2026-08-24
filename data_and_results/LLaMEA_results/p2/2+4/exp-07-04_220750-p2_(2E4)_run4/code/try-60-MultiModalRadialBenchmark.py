import numpy as np

class MultiModalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-1, 1, (10, dim))
        self.weights = np.random.exponential(1, 10)
        self.weights = self.weights / np.sum(self.weights)
    
    def f(self, x):
        x_norm = x / 5.0
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            dist = np.sum((x_norm - center)**2)
            rbf_sum += self.weights[i] * np.exp(-5 * dist)
        
        # Sinusoidal coupling terms
        sin_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j] * np.pi) * np.cos(0.5 * (x_norm[i]**2 + x_norm[j]**2))
                sin_coupling += coupling
        
        # Adaptive conditioning with exponential scaling
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += np.exp(0.5 * x_norm[i]**2) * np.sin(3 * x_norm[i] * np.pi)
        
        # Cross-dimensional polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3) * (x_norm[j]**2) * np.sin(2 * np.pi * x_norm[i] * x_norm[j])
        
        # Saddle point creation with hyperbolic tangent
        tanh_saddle = 0.0
        for i in range(self.dim):
            tanh_saddle += np.tanh(x_norm[i] * 2) * np.cos(0.3 * x_norm[i]**2)
        
        # Combined fitness function
        return rbf_sum + 0.2 * sin_coupling + 0.15 * cond_sum + 0.25 * poly_interaction + 0.1 * tanh_saddle