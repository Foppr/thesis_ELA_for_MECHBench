import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        poly_term = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6)
        
        # Trigonometric component with multiple frequencies
        trig_term = 0.0
        for i in range(self.dim):
            freqs = [1, 2, 3, 4, 5]
            for freq in freqs:
                trig_term += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial basis function component with adaptive scaling
        rbf_term = 0.0
        for i in range(self.dim):
            rbf_term += np.exp(-2.0 * (x_norm[i] - 0.5)**2) + np.exp(-1.5 * (x_norm[i] + 0.3)**2)
        
        # Cross-dimensional interaction with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = 1.0 + 0.3 * np.sin(3 * np.pi * dist)
                cross_term += coupling * np.exp(-dist**2)
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.2 * self.dim + 0.1 * np.sin(np.pi * self.dim / 2.0)
        
        # Combine all terms with dynamic weights
        result = cond_factor * (0.4 * poly_term + 0.3 * trig_term + 0.2 * rbf_term + 0.1 * cross_term)
        
        return result