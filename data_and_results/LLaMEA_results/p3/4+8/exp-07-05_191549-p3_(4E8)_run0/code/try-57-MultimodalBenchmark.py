import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple chaotic sine waves
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(15 * np.pi * r) * np.cos(8 * np.pi * r) * np.sin(5 * np.pi * r) * np.exp(-0.5 * r**2)
        
        # Multi-dimensional chaotic sine wave interactions
        chaotic_term = np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled) * 
                             np.sin(12 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Adaptive polynomial conditioning with exponential barrier
        adaptive_poly = np.sum((x_scaled**6 - 3*x_scaled**4 + 3*x_scaled**2 - 1) * 
                              (1 + 0.3 * r**2) * np.exp(-0.1 * r**2))
        
        # Cross-term interactions with radial modulation and additional barrier
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x_scaled[i] * x_scaled[i+1] * 
                          np.sin(20 * np.pi * x_scaled[i]) * 
                          np.cos(10 * np.pi * x_scaled[i+1]) * 
                          np.exp(-1.5 * r**2) * 
                          (1 + 0.2 * np.sin(5 * np.pi * x_scaled[i])))
        
        # Additional exponential barrier term
        barrier_term = np.exp(-2 * r**2) * np.sum(x_scaled**2)
        
        # Combine all terms with different weights
        return 0.25 * radial_term + 0.35 * chaotic_term + 0.2 * adaptive_poly + 0.15 * cross_term + 0.05 * barrier_term