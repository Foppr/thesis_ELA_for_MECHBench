import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic periodic terms with modified frequencies and amplitudes
        chaotic = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * 
                         np.sin(4 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Exponential decay with logarithmic modification for flat regions
        exponential = np.sum(np.exp(-0.3 * x_scaled**2) * (1.0 + 0.15 * np.log(1.0 + x_scaled**2)))
        
        # Saddle point interaction term between dimensions with modified coefficients
        saddle = np.sum((x_scaled[:-1]**2 - x_scaled[1:]**2) * (x_scaled[:-1] + x_scaled[1:]) * 0.5)
        
        # Nonlinear interaction with different cubic terms
        cubic_interaction = np.sum(x_scaled[:-2]**2 * x_scaled[1:-1] * x_scaled[2:]**2)
        
        # Additional radial symmetry term with higher frequency
        radial = np.sum(np.sin(10 * np.pi * np.sqrt(np.sum(x_scaled**2))) * np.cos(8 * np.pi * np.sqrt(np.sum(x_scaled**2))))
        
        # Combine all terms with different weights
        return 0.15 * quadratic + 0.45 * chaotic + 0.25 * exponential + 0.1 * saddle + 0.05 * cubic_interaction + 0.05 * radial + 2.5