import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial quadratic term for conditioning and global attraction
        radial = np.sum(x_scaled**2)
        
        # Periodic potential wells with varying frequencies and amplitudes
        periodic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled) * 
                         np.sin(6 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Chaotic interaction terms between dimensions
        chaotic_interaction = np.sum(np.sin(np.pi * x_scaled[:-1] * x_scaled[1:]) * 
                                   np.cos(2 * np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Exponential decay with trigonometric modulation for flat regions
        exponential_mod = np.sum(np.exp(-0.3 * x_scaled**2) * (1.0 + 0.2 * np.sin(5 * x_scaled)))
        
        # Cross-dimensional coupling with sine-cosine interaction
        coupling = np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * np.cos(x_scaled[:-1] - x_scaled[1:]))
        
        # Nonlinear transformation with polynomial and logarithmic terms
        nonlinear = np.sum((x_scaled**4 + 0.1 * x_scaled**3 + 0.01 * x_scaled**2) * 
                          (1.0 + 0.1 * np.log(1.0 + x_scaled**2)))
        
        # Combine all terms with different weights
        return 0.2 * radial + 0.4 * periodic + 0.1 * chaotic_interaction + 0.1 * exponential_mod + 0.1 * coupling + 0.1 * nonlinear + 2.0