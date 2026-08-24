import numpy as np

class HybridOscillatoryRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillatory frequencies and radial centers
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.attraction_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component
        sin_component = np.sum(np.sin(self.frequencies * x_norm) * np.cos(2 * self.frequencies * x_norm))
        
        # Radial basis function component with dynamic widths
        rbf_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.rbf_centers[i])**2)
            width = 0.5 + 0.5 * np.sin(i)
            rbf_sum += np.exp(-dist / (2 * width**2))
        
        # Gradient-based attraction fields
        attraction_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.attraction_centers[i])**2)
            attraction_sum += 1.0 / (1.0 + dist)
        
        # Polynomial coupling terms
        poly_term = np.sum(x_norm**2 + 0.3 * x_norm**4 + 0.05 * x_norm**6)
        
        # Sharp transition zones using hyperbolic tangent
        transition_term = np.sum(np.tanh(10 * (x_norm - 0.5)) * np.tanh(10 * (x_norm + 0.5)))
        
        # Combine all components with adaptive weights
        total = 0.25 * sin_component + 0.3 * rbf_sum + 0.2 * attraction_sum + 0.15 * poly_term + 0.1 * transition_term
        
        # Add a global conditioning factor
        conditioning = 1.0 + 0.3 * np.sin(np.sum(x_norm**3))
        
        return total * conditioning