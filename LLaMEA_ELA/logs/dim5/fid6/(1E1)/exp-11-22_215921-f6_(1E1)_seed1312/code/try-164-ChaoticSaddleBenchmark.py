import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component with dynamic frequency modulation
        chaotic_wave = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.3 * np.sin(5 * x_norm))) * 
                             np.exp(-0.5 * x_norm**2))
        
        # Radial basis function with adaptive variance and position
        rbf = 0.0
        for i in range(self.dim):
            sigma = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            center = 0.3 * np.sin(i * np.pi / self.dim)
            rbf += np.exp(-0.5 * ((x_norm[i] - center) / sigma)**2)
        
        # Gradient-based saddle structure with alternating sign patterns
        saddle = 0.0
        for i in range(self.dim - 1):
            grad_term = (x_norm[i+1] - x_norm[i])**2
            sign = (-1)**i
            saddle += sign * grad_term * np.exp(-0.3 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Multi-scale periodic modulation with varying amplitudes
        multi_scale = 0.0
        for scale in [1, 2, 4]:
            multi_scale += np.sum(np.sin(scale * np.pi * x_norm) * 
                                np.cos(scale * np.pi * x_norm) * 
                                np.exp(-0.2 * x_norm**2))
        
        # Asymmetric elliptical valley with directional conditioning
        ellipse_valley = 0.0
        for i in range(self.dim - 1):
            ellipse_valley += (x_norm[i]**2 + 0.3 * x_norm[i+1]**2) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Dimension-dependent conditioning factor with exponential decay
        condition_factor = 1.0 + 0.8 * np.exp(-0.1 * self.dim)
        
        # Combine all terms with different weights
        return condition_factor * (chaotic_wave + 0.5 * rbf + 0.3 * saddle + 
                                 0.4 * multi_scale + 0.6 * ellipse_valley)