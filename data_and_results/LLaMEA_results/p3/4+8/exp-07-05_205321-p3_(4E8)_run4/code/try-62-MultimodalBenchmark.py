import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic periodic terms with modified frequencies
        chaotic = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * 
                         np.sin(4 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) * 
                         np.sin(8 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Exponential decay with logarithmic modification for flat regions
        exponential = np.sum(np.exp(-0.3 * x_scaled**2) * (1.0 + 0.15 * np.log(1.0 + x_scaled**2)))
        
        # Modified saddle point interaction term with cross-dimensional coupling
        saddle = np.sum((x_scaled[:-1]**2 - x_scaled[1:]**2) * (x_scaled[:-1] + x_scaled[1:]) * 
                       (1.0 + 0.12 * np.sin(4 * np.pi * x_scaled[:-1]) * np.cos(4 * np.pi * x_scaled[1:])))
        
        # Additional cubic interaction with higher-order cross-dimensional coupling
        cubic_interaction = np.sum(x_scaled[:-2]**3 * x_scaled[1:-1] * x_scaled[2:] * 
                                  (1.0 + 0.08 * np.sin(6 * np.pi * x_scaled[:-2]) * 
                                   np.cos(6 * np.pi * x_scaled[1:-1]) * 
                                   np.sin(6 * np.pi * x_scaled[2:])))
        
        # Additional high-frequency modulation for increased complexity
        high_freq = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Combine all terms with optimized weights
        return 0.12 * quadratic + 0.55 * chaotic + 0.18 * exponential + 0.12 * saddle + 0.08 * cubic_interaction + 0.05 * high_freq + 3.0