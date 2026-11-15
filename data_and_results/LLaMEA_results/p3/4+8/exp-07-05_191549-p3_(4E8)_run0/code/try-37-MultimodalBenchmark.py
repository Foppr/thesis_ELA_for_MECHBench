import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with chaotic sine waves
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(10 * np.pi * r) * np.cos(5 * np.pi * r) * np.sin(3 * np.pi * r)
        
        # Chaotic sine wave interactions
        chaotic_term = np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled))
        
        # Adaptive polynomial conditioning based on distance from origin
        adaptive_poly = np.sum((x_scaled**4 - 2*x_scaled**2 + 1) * (1 + 0.5 * r))
        
        # Cross-term interactions with radial modulation
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x_scaled[i] * x_scaled[i+1] * 
                          np.sin(12 * np.pi * x_scaled[i]) * 
                          np.cos(6 * np.pi * x_scaled[i+1]) * 
                          np.exp(-2 * r))
        
        # Combine all terms with different weights
        return 0.3 * radial_term + 0.4 * chaotic_term + 0.2 * adaptive_poly + 0.1 * cross_term