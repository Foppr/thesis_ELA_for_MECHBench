import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with enhanced chaotic sine waves
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(15 * np.pi * r) * np.cos(7 * np.pi * r) * np.sin(4 * np.pi * r)
        
        # Enhanced chaotic sine wave interactions with exponential modulation
        chaotic_term = np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled) * 
                             np.sin(10 * np.pi * x_scaled) * np.exp(-3 * r))
        
        # Adaptive polynomial conditioning with cubic terms and exponential barrier
        adaptive_poly = np.sum((x_scaled**6 - 3*x_scaled**4 + 3*x_scaled**2 - 1) * 
                              (1 + 0.3 * r + 0.1 * r**2))
        
        # Cross-term interactions with additional trigonometric modulation
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x_scaled[i] * x_scaled[i+1] * 
                          np.sin(15 * np.pi * x_scaled[i]) * 
                          np.cos(8 * np.pi * x_scaled[i+1]) * 
                          np.exp(-3 * r) * np.sin(5 * np.pi * r))
        
        # Additional exponential barrier term to increase conditioning
        barrier_term = np.sum(np.exp(-5 * (x_scaled**2)) * np.sin(2 * np.pi * x_scaled))
        
        # Combine all terms with modified weights
        return 0.25 * radial_term + 0.35 * chaotic_term + 0.25 * adaptive_poly + 0.1 * cross_term + 0.05 * barrier_term