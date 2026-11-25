import numpy as np

class RuggedGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like chaotic corridors with varying decay rates
        corridor_term = 0.0
        for i in range(self.dim):
            decay_rate = 2.0 + 1.5 * np.sin(7.0 * x_scaled[i])
            corridor_term += np.exp(-np.abs(x_scaled[i]) * decay_rate) * np.sin(8.0 * x_scaled[i])
        
        # Multi-scale Gaussian hills with fractal-like dimensions
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 2.0 + 0.5 * np.sin(6.0 * x_scaled[i]) + 0.3 * np.cos(9.0 * x_scaled[i])
            width = 0.25 + 0.4 * np.sin(5.0 * x_scaled[i])**2
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Adaptive gradient modulation with fractal scaling
        grad_mod = 1.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.5 * np.sin(10.0 * x_scaled[i]) * np.cos(7.0 * x_scaled[i])
            grad_mod *= (1.0 + 0.4 * mod_factor)
        
        # Cross-dimensional interaction with fractal coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.sin(6.5 * (x_scaled[i] + x_scaled[j]))
                coupling_term += coupling_strength * np.sin(12.0 * (x_scaled[i] - x_scaled[j]))
        
        # Extreme ruggedness through multi-frequency chaotic oscillations
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += (np.sin(35.0 * x_scaled[i]) * np.cos(28.0 * x_scaled[i]) + 
                          0.7 * np.sin(42.0 * x_scaled[i]) * np.cos(33.0 * x_scaled[i]))
        
        # Combined result with fractal weighting and conditioning
        result = (0.25 * corridor_term + 
                 0.35 * gaussian_term + 
                 0.25 * coupling_term + 
                 0.15 * ruggedness) * grad_mod
        
        return result