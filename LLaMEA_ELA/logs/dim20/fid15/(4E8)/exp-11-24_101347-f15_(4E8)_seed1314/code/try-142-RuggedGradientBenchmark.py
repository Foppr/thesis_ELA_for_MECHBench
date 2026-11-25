import numpy as np

class RuggedGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multi-scale fractal corridor structures with varying decay rates
        corridor_term = 0.0
        for i in range(self.dim):
            corridor_term += (np.exp(-np.abs(x_scaled[i]) * 3.8) * 
                            np.sin(8.2 * x_scaled[i]) * 
                            np.cos(2.9 * x_scaled[i]) * 
                            np.sin(4.7 * x_scaled[i]))
        
        # Adaptive Gaussian hill structures with dynamic parameters
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 1.9 + 0.5 * np.sin(7.1 * x_scaled[i]) + 0.3 * np.cos(5.2 * x_scaled[i])
            width = 0.5 + 0.25 * np.sin(6.8 * x_scaled[i]) + 0.15 * np.cos(4.1 * x_scaled[i])
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Enhanced adaptive gradient modulation with multi-frequency components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1.0 + 0.4 * np.sin(7.3 * x_scaled[i]) + 
                        0.3 * np.cos(9.1 * x_scaled[i]) + 
                        0.2 * np.sin(13.2 * x_scaled[i]))
        
        # Complex cross-dimensional interaction with fractal coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.9 + 0.25 * np.sin(4.8 * (x_scaled[i] + x_scaled[j])) + \
                                  0.18 * np.cos(6.7 * (x_scaled[i] - x_scaled[j]))
                coupling_term += coupling_strength * np.sin(9.8 * (x_scaled[i] - x_scaled[j]) + 
                                                           4.2 * np.cos(5.9 * (x_scaled[i] + x_scaled[j])))
        
        # Ultra-ruggedness through fractal-like oscillations and noise
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += (np.sin(35.0 * x_scaled[i]) * np.cos(30.0 * x_scaled[i]) + 
                          0.6 * np.sin(52.0 * x_scaled[i]) * np.cos(42.0 * x_scaled[i]) + 
                          0.4 * np.sin(68.0 * x_scaled[i]))
        
        # Additional chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.18 * np.sin(27.0 * x_scaled[i] + 1.3) * np.cos(19.0 * x_scaled[i] + 0.7)
        
        # Combined result with dynamic weighting and fractal scaling
        result = (0.30 * corridor_term + 
                 0.32 * gaussian_term + 
                 0.23 * coupling_term + 
                 0.12 * ruggedness + 
                 0.03 * noise) * grad_mod
        
        return result