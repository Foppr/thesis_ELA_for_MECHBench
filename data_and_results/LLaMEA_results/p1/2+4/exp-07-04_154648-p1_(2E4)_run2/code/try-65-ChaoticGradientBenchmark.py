import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic control parameters
        self.chaos_params = np.random.uniform(0.1, 0.9, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.penalty_centers = np.random.uniform(-5.0, 5.0, (5, dim))
        self.penalty_radii = np.random.uniform(0.5, 2.0, 5)
        
    def f(self, x):
        x_norm = x / 5.0
        # Chaotic gradient component
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += (np.sin(self.chaos_params[i] * x_norm[i]) * 
                           np.cos(self.chaos_params[i] * x_norm[i] * 2.0)) * \
                           (1.0 + 0.3 * np.sin(3.0 * x_norm[i]))
        
        # Saddle-point structure with varying curvature
        saddle_term = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            # Create saddle-like behavior with mixed positive/negative curvature
            curvature = np.sin(np.sum(diff**2) * 0.5) * 0.5 + 0.5
            saddle_term += curvature * np.sum(diff**2) * np.exp(-0.5 * np.sum(diff**2))
        
        # Adaptive penalty regions
        penalty = 0.0
        for i in range(5):
            diff = x_norm - self.penalty_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            if distance < self.penalty_radii[i]:
                penalty += 10.0 * np.exp(-0.5 * (distance / self.penalty_radii[i])**2)
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (np.sin(x_norm[i] * x_norm[i+1]) * 
                             np.cos(x_norm[i] + x_norm[i+1]) * 
                             np.exp(-0.1 * np.abs(x_norm[i] - x_norm[i+1])))
        
        # Polynomial and trigonometric mixture for complexity
        poly_term = 0.02 * np.sum(x_norm**4)
        trig_term = 0.03 * np.sum(np.sin(2.0 * x_norm)**2)
        
        # Global minimum at origin with additional chaotic modulation
        base_value = 0.5 * np.sum(x_norm**2)
        chaotic_mod = 0.3 * np.sin(np.sum(x_norm**3))
        
        return base_value + chaotic_grad + saddle_term + penalty + cross_coupling + poly_term + trig_term + chaotic_mod