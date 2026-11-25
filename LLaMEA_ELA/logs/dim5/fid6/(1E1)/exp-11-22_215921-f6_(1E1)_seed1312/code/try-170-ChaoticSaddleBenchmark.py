import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(10 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * 
                             np.exp(-0.2 * x_norm**2))
        
        # Radial basis function with adaptive centers and widths
        rbfs = 0.0
        for i in range(min(self.dim, 10)):
            center = 0.5 * np.sin(i * np.pi / 5.0)
            width = 0.3 + 0.2 * np.cos(i * np.pi / 4.0)
            rbfs += np.exp(-width * (x_norm - center)**2)
        
        # Gradient-based saddle structure with cross-dimensional interactions
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x_norm[i] * x_norm[i+1]) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Multi-scale oscillatory pattern with exponential decay
        multi_scale = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                            np.exp(-0.3 * x_norm**2) * (1.0 + 0.2 * np.sin(5 * x_norm)))
        
        # Dynamic conditioning factor with periodic modulation
        condition_factor = 1.5 + 0.8 * np.sin(0.5 * self.dim)
        
        # Combine all terms with dimension-dependent weighting
        return condition_factor * (chaotic_wave + rbfs + saddle + multi_scale)