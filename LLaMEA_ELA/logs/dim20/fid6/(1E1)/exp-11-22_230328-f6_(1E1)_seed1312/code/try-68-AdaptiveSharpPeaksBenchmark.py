import numpy as np

class AdaptiveSharpPeaksBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for performance
        self.constants = {
            'poly_weights': np.random.uniform(0.5, 2.0, dim),
            'freq_weights': np.random.uniform(1.0, 8.0, dim),
            'peak_positions': np.random.uniform(-5.0, 5.0, (3, dim)),
            'sharpness_factors': np.random.uniform(10.0, 50.0, 3)
        }
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial component with adaptive weights
        poly_term = np.sum(self.constants['poly_weights'] * (x_norm ** 4))
        
        # Trigonometric modulation with varying frequencies
        trig_term = np.sum(np.sin(self.constants['freq_weights'] * x_norm) * 
                          np.cos(self.constants['freq_weights'] * x_norm))
        
        # Neural-inspired radial basis function with sharp peaks
        rbf_sum = 0.0
        for i in range(3):
            peak_pos = self.constants['peak_positions'][i]
            sharpness = self.constants['sharpness_factors'][i]
            dist = np.sum((x_norm - peak_pos / 5.0) ** 2)
            rbf_sum += np.exp(-sharpness * dist)
        
        # Adaptive conditioning based on input magnitude
        condition_factor = 1.0 + 0.5 * np.tanh(np.sum(x_norm**2) - self.dim / 2.0)
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2) * \
                         (1 + 0.3 * np.sin(5 * (x_norm[i] + x_norm[i+1])))
        
        # Global scaling and final composition
        return condition_factor * (poly_term + trig_term + rbf_sum + cross_term)