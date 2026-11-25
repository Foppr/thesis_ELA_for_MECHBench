import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with periodic modulations
        r = np.sqrt(np.sum(x_norm**2, axis=0))
        radial_term = np.sin(10 * r) * np.cos(7 * r) * np.exp(-0.5 * r**2)
        
        # Angular periodic components
        angles = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else np.array([0.0])
        angular_term = np.sin(15 * angles) * np.cos(12 * angles)
        
        # Multi-scale oscillatory pattern
        oscillation = np.sum(np.sin(20 * x_norm) * np.cos(18 * x_norm) * 
                           (1 + 0.3 * np.sin(14 * x_norm)) * 
                           (1 + 0.2 * np.cos(10 * x_norm)))
        
        # Adaptive conditioning based on distance from origin
        condition_factor = 1.0 + 0.5 * np.exp(-r**2) + 0.3 * np.sin(5 * r)
        
        # Composite multimodal structure with varying curvature
        multimodal = np.sum((x_norm**4) * (1 + 0.4 * np.sin(8 * x_norm)) * 
                           (1 + 0.3 * np.cos(6 * x_norm)) * 
                           (1 + 0.2 * np.sin(4 * x_norm)))
        
        # Combined function with dynamic scaling
        return condition_factor * (radial_term + angular_term + oscillation + multimodal)