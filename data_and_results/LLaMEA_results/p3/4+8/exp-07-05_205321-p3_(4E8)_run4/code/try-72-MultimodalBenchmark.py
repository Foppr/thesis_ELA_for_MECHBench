import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial quadratic term for conditioning
        r_squared = np.sum(x_scaled**2)
        radial = r_squared * np.exp(-0.1 * r_squared)
        
        # Chaotic trigonometric interactions with varying frequencies
        trig_interaction = np.sum(np.sin(10 * x_scaled) * np.cos(15 * x_scaled) * 
                                np.sin(7 * x_scaled) * np.cos(12 * x_scaled))
        
        # Coupled sine waves with phase shifts
        coupled_sines = np.sum(np.sin(5 * x_scaled + np.pi/4) * 
                             np.sin(3 * x_scaled + np.pi/3) * 
                             np.sin(8 * x_scaled + np.pi/6))
        
        # Exponentially decaying harmonic components with noise
        noise_mod = np.sum(np.exp(-2 * np.abs(x_scaled)) * 
                          (1.0 + 0.2 * np.sin(20 * x_scaled) * np.cos(15 * x_scaled)))
        
        # Saddle point interactions with radial dependence
        saddle = np.sum((x_scaled[:-1]**2 - x_scaled[1:]**2) * 
                       np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Higher-order polynomial interactions
        poly_interaction = np.sum(x_scaled[:-2]**4 * x_scaled[1:-1]**2 * x_scaled[2:]**3)
        
        # Add chaotic modulation based on angular coordinates
        angles = np.arctan2(x_scaled[1:], x_scaled[:-1])
        angular_mod = np.sum(np.sin(20 * angles) * np.cos(15 * angles))
        
        # Combine all terms with different weights
        return 0.2 * radial + 0.4 * trig_interaction + 0.15 * coupled_sines + 0.1 * noise_mod + 0.05 * saddle + 0.05 * poly_interaction + 0.05 * angular_mod + 2.0