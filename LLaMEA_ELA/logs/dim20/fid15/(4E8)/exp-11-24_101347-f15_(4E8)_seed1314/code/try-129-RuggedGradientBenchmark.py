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
            corridor_term += (np.exp(-np.abs(x_scaled[i]) * 4.2) * 
                            np.sin(7.8 * x_scaled[i]) * 
                            np.cos(3.1 * x_scaled[i]) * 
                            np.sin(5.3 * x_scaled[i]))
        
        # Adaptive Gaussian hill structures with dynamic parameters
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 2.1 + 0.4 * np.sin(6.2 * x_scaled[i]) + 0.2 * np.cos(4.7 * x_scaled[i])
            width = 0.45 + 0.3 * np.sin(5.9 * x_scaled[i]) + 0.1 * np.cos(3.8 * x_scaled[i])
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Enhanced adaptive gradient modulation with multi-frequency components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1.0 + 0.45 * np.sin(6.8 * x_scaled[i]) + 
                        0.25 * np.cos(8.3 * x_scaled[i]) + 
                        0.15 * np.sin(12.7 * x_scaled[i]))
        
        # Complex cross-dimensional interaction with fractal coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.3 * np.sin(5.2 * (x_scaled[i] + x_scaled[j])) + \
                                  0.2 * np.cos(7.4 * (x_scaled[i] - x_scaled[j]))
                coupling_term += coupling_strength * np.sin(10.5 * (x_scaled[i] - x_scaled[j]) + 
                                                           3.7 * np.cos(6.1 * (x_scaled[i] + x_scaled[j])))
        
        # Ultra-ruggedness through fractal-like oscillations and noise
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += (np.sin(32.0 * x_scaled[i]) * np.cos(27.0 * x_scaled[i]) + 
                          0.5 * np.sin(48.0 * x_scaled[i]) * np.cos(39.0 * x_scaled[i]) + 
                          0.3 * np.sin(61.0 * x_scaled[i]))
        
        # Additional chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.2 * np.sin(25.0 * x_scaled[i] + 1.5) * np.cos(18.0 * x_scaled[i] + 0.8)
        
        # Combined result with dynamic weighting and fractal scaling
        result = (0.28 * corridor_term + 
                 0.35 * gaussian_term + 
                 0.25 * coupling_term + 
                 0.10 * ruggedness + 
                 0.02 * noise) * grad_mod
        
        return result