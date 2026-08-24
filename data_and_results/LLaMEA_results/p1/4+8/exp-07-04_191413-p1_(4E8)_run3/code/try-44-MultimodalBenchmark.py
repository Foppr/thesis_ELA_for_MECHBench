import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine wave component with time-varying frequency
        chaotic_term = np.sum(np.sin(10 * np.pi * x_scaled * (1 + 0.1 * np.sin(5 * x_scaled)))**2)
        
        # Gradient-based quadratic with adaptive conditioning
        adaptive_quad = np.sum((x_scaled**2) * (1 + 0.5 * np.sin(2 * np.pi * x_scaled)))
        
        # Harmonic oscillations with varying amplitudes and phases
        harmonic_osc = np.sum(np.cos(4 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                             0.6 * np.cos(8 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2) + 
                             0.3 * np.cos(12 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = np.sum(np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                               np.sin(np.pi * (x_scaled[:-1] + x_scaled[1:]))**2)
        
        # Saddle-point attractor terms
        saddle_attractor = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.8 * adaptive_quad + 0.6 * chaotic_term + 0.5 * harmonic_osc + 0.3 * cross_coupling + 0.2 * saddle_attractor