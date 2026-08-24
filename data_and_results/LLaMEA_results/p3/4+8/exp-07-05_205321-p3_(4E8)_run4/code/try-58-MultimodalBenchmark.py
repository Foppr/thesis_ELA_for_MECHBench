import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic periodic terms with higher frequency components
        chaotic = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * 
                         np.sin(4 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) * 
                         np.sin(8 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Exponential decay with logarithmic modification for flat regions
        exponential = np.sum(np.exp(-0.3 * x_scaled**2) * (1.0 + 0.15 * np.log(1.0 + x_scaled**2)))
        
        # Enhanced saddle point interaction term between dimensions
        saddle = np.sum((x_scaled[:-1]**2 - x_scaled[1:]**2) * (x_scaled[:-1] + x_scaled[1:]) * 
                       (1.0 + 0.15 * np.abs(x_scaled[:-1] * x_scaled[1:])))
        
        # Nonlinear interaction with higher-order terms
        cubic_interaction = np.sum(x_scaled[:-2]**3 * x_scaled[1:-1] * x_scaled[2:] * 
                                 (1.0 + 0.08 * np.abs(x_scaled[:-2] + x_scaled[1:-1] + x_scaled[2:])))
        
        # Additional high-frequency sinusoidal modulation
        modulation = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled))
        
        # Radial bias term to create more pronounced global optimum
        radial_bias = 0.2 * np.sum(x_scaled**4)
        
        # Combine all terms with different weights
        return 0.1 * quadratic + 0.55 * chaotic + 0.2 * exponential + 0.1 * saddle + 0.05 * cubic_interaction + 0.05 * modulation + 0.1 * radial_bias + 3.0