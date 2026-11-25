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
            corridor_term += (np.exp(-np.abs(x_scaled[i]) * 4.5) * 
                            np.sin(8.2 * x_scaled[i]) * 
                            np.cos(3.5 * x_scaled[i]) * 
                            np.sin(5.7 * x_scaled[i]))
        
        # Adaptive Gaussian hill structures with dynamic parameters
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 2.3 + 0.45 * np.sin(6.5 * x_scaled[i]) + 0.25 * np.cos(4.9 * x_scaled[i])
            width = 0.5 + 0.35 * np.sin(6.1 * x_scaled[i]) + 0.15 * np.cos(3.9 * x_scaled[i])
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Enhanced adaptive gradient modulation with multi-frequency components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1.0 + 0.5 * np.sin(7.1 * x_scaled[i]) + 
                        0.3 * np.cos(8.7 * x_scaled[i]) + 
                        0.2 * np.sin(13.2 * x_scaled[i]))
        
        # Complex cross-dimensional interaction with fractal coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.85 + 0.35 * np.sin(5.5 * (x_scaled[i] + x_scaled[j])) + \
                                  0.25 * np.cos(7.8 * (x_scaled[i] - x_scaled[j]))
                coupling_term += coupling_strength * np.sin(11.0 * (x_scaled[i] - x_scaled[j]) + 
                                                           4.0 * np.cos(6.5 * (x_scaled[i] + x_scaled[j])))
        
        # Ultra-ruggedness through fractal-like oscillations and noise
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += (np.sin(35.0 * x_scaled[i]) * np.cos(30.0 * x_scaled[i]) + 
                          0.55 * np.sin(52.0 * x_scaled[i]) * np.cos(42.0 * x_scaled[i]) + 
                          0.35 * np.sin(65.0 * x_scaled[i]))
        
        # Additional chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.25 * np.sin(27.0 * x_scaled[i] + 1.6) * np.cos(19.0 * x_scaled[i] + 0.9)
        
        # Combined result with dynamic weighting and fractal scaling
        result = (0.3 * corridor_term + 
                 0.38 * gaussian_term + 
                 0.22 * coupling_term + 
                 0.12 * ruggedness + 
                 0.025 * noise) * grad_mod
        
        return result