import numpy as np

class RadialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute some constants for the landscape
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_result = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            weight = self.rbf_weights[i]
            distance = np.sum((x - center)**2)
            rbf_result += weight * np.exp(-0.5 * distance / (self.dim + 1))
        
        # Trigonometric corridor component
        trig_result = 0.0
        for i in range(self.dim):
            trig_result += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Adaptive conditioning based on distance from center
        dist_from_origin = np.linalg.norm(x)
        conditioning_factor = 1.0 + 0.5 * np.sin(dist_from_origin)
        
        # Cross-dimensional interaction with corridor structure
        cross_result = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_result += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                               np.exp(-0.05 * (x[i]**2 + x[j]**2)) * conditioning_factor
                
        # Add a global sinusoidal modulation
        global_modulation = np.sin(0.5 * dist_from_origin) * np.cos(0.3 * dist_from_origin)
        
        # Combine all components with different weights
        result = 0.8 * rbf_result + 0.6 * trig_result + 0.4 * cross_result + \
                 0.2 * global_modulation + 0.1 * np.sum(x**4) * conditioning_factor
        
        return result