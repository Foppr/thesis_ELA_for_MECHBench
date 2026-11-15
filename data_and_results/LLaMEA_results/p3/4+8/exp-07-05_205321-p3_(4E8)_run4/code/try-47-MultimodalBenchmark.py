import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Highly chaotic periodic terms with varying frequencies and amplitudes
        chaotic = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) * 
                         np.sin(3 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Exponential decay with logarithmic modification for flat regions
        exponential = np.sum(np.exp(-0.5 * x_scaled**2) * (1.0 + 0.1 * np.log(1.0 + x_scaled**2)))
        
        # Saddle point interaction term between dimensions
        saddle = np.sum((x_scaled[:-1]**2 - x_scaled[1:]**2) * (x_scaled[:-1] + x_scaled[1:]))
        
        # Nonlinear interaction with cubic terms
        cubic_interaction = np.sum(x_scaled[:-2]**3 * x_scaled[1:-1] * x_scaled[2:])
        
        # Radial symmetry term with multiple peaks
        radial = np.sum(np.sin(10 * np.pi * np.sqrt(np.sum(x_scaled**2))) * 
                       np.exp(-0.1 * np.sum(x_scaled**2)))
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_coupling = np.sum(np.sin(np.pi * x_scaled[:-1]) * np.cos(np.pi * x_scaled[1:]) * 
                               (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # High-frequency oscillation term
        high_freq = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.1 * quadratic + 0.4 * chaotic + 0.15 * exponential + 0.1 * saddle + 0.1 * cubic_interaction + 0.1 * radial + 0.05 * cross_coupling + 0.05 * high_freq + 3.0