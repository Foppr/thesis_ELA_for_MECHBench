import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic base function
        quadratic_base = np.sum(x_norm**2)
        
        # Non-separable correlation term using a modified Ackley-like interaction
        correlation_term = -20 * np.exp(-0.2 * np.sqrt(np.mean(x_norm**2))) - \
                           np.exp(np.mean(np.cos(2 * np.pi * x_norm))) + 20 + np.e
        
        # Helicoidal chaotic distortion with varying pitch
        helix_distortion = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix_distortion += np.sin(7 * angle + i * 0.3) * np.cos(7 * angle + i * 0.3)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        modulated_term = np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * 
                               np.sin(4 * x_norm) * np.cos(3 * x_norm))
        
        # Fractal-like basin with multiple local minima, shifted and scaled
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 0.7 * np.exp(-r**2) + 0.4 * np.sin(12 * r) * np.cos(6 * r) - 0.2
        
        # Combined function with adaptive scaling
        return 0.4 * quadratic_base + 0.4 * correlation_term + \
               0.15 * helix_distortion + 0.05 * modulated_term + fractal_basin