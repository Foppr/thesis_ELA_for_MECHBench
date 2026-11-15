import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-order polynomial conditioning with saddle points
        poly_term = np.sum(0.5 * x_scaled**8 - 2 * x_scaled**6 + 3 * x_scaled**4 - 1.5 * x_scaled**2)
        
        # Chaotic sinusoidal interactions with irrational frequencies
        sin_term = np.sum(np.sin(np.pi * np.sqrt(2) * x_scaled) * 
                         np.sin(np.pi * np.e * x_scaled) * 
                         np.sin(np.pi * np.sqrt(3) * x_scaled) * 
                         np.sin(np.pi * np.pi * x_scaled))
        
        # Adaptive exponential barriers with varying steepness
        exp_barrier = np.sum(np.exp(-10 * np.abs(x_scaled)) * 
                           np.sin(25 * np.pi * x_scaled)**4 + 
                           np.exp(-15 * np.abs(x_scaled)) * 
                           np.cos(30 * np.pi * x_scaled)**4)
        
        # Cross-term with chaotic coupling
        cross_term = np.sum(np.sin(12 * np.pi * x_scaled[:-1]) * 
                          np.cos(18 * np.pi * x_scaled[1:]) * 
                          np.sin(24 * np.pi * x_scaled[:-1] * x_scaled[1:]) * 
                          x_scaled[:-1] * x_scaled[1:])
        
        # Additional chaotic modulation
        chaos_mod = np.sum(np.sin(7 * np.pi * x_scaled) * 
                          np.cos(11 * np.pi * x_scaled) * 
                          np.sin(13 * np.pi * x_scaled) * 
                          np.cos(17 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.3 * poly_term + 0.25 * sin_term + 0.2 * exp_barrier + 0.15 * cross_term + 0.1 * chaos_mod