import numpy as np

class RuggedGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced fractal-like corridor structures with multi-scale decay
        corridor_term = 0.0
        for i in range(self.dim):
            corridor_term += (np.exp(-np.abs(x_scaled[i]) * 2.5) * 
                            np.sin(7.0 * x_scaled[i]) * 
                            np.cos(3.0 * x_scaled[i]))
        
        # Modified Gaussian structures with dynamic parameters and radial interaction
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 1.2 + 0.5 * np.sin(5.0 * x_scaled[i])
            width = 0.2 + 0.6 * np.cos(4.0 * x_scaled[i])
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Enhanced gradient modulation with non-linear scaling
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1.0 + 0.5 * np.sin(6.0 * x_scaled[i]) * 
                        np.cos(2.0 * x_scaled[i]))
        
        # Multi-scale coupling with fractal-like interaction patterns
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.cos(5.0 * (x_scaled[i] + x_scaled[j]))
                coupling_term += coupling_strength * np.sin(9.0 * (x_scaled[i] - x_scaled[j]))
        
        # Enhanced ruggedness with combined high-frequency oscillations
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += (np.sin(30.0 * x_scaled[i]) * 
                          np.cos(25.0 * x_scaled[i]) * 
                          np.sin(15.0 * x_scaled[i]))
        
        # Cross-dimensional interaction with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                coupling = 0.7 + 0.3 * np.sin(8.0 * dist)
                cross_term += coupling * np.exp(-2.0 * dist**2) * np.cos(10.0 * (x_scaled[i] + x_scaled[j]))
        
        # Combined result with refined dynamic weighting
        result = (0.25 * corridor_term + 
                 0.35 * gaussian_term + 
                 0.2 * coupling_term + 
                 0.15 * ruggedness + 
                 0.05 * cross_term) * grad_mod
        
        return result