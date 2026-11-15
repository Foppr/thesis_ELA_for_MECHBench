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
        chaotic = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) * 
                         np.sin(3 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * 
                         np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Exponential decay with logarithmic modification for flat regions
        exponential = np.sum(np.exp(-0.5 * x_scaled**2) * (1.0 + 0.1 * np.log(1.0 + x_scaled**2)))
        
        # Enhanced saddle point interaction term between dimensions with modified coefficients
        saddle = np.sum((x_scaled[:-1]**2 - x_scaled[1:]**2) * (x_scaled[:-1] + x_scaled[1:]) * 
                       (1.0 + 0.2 * np.abs(x_scaled[:-1] * x_scaled[1:])))
        
        # Nonlinear interaction with higher-order terms and increased complexity
        cubic_interaction = np.sum(x_scaled[:-2]**3 * x_scaled[1:-1] * x_scaled[2:] * 
                                 (1.0 + 0.1 * np.abs(x_scaled[:-2] + x_scaled[1:-1] + x_scaled[2:])))
        
        # Additional high-frequency sinusoidal modulation with increased frequency
        modulation = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Add a new term with cross-dimensional interactions and exponential scaling
        cross_term = np.sum(np.exp(-0.3 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                           (x_scaled[:-1] * x_scaled[1:]) * 
                           (1.0 + 0.15 * np.abs(x_scaled[:-1] - x_scaled[1:])))
        
        # Combine all terms with different weights
        return 0.1 * quadratic + 0.55 * chaotic + 0.15 * exponential + 0.1 * saddle + 0.05 * cubic_interaction + 0.05 * modulation + 0.05 * cross_term + 3.0