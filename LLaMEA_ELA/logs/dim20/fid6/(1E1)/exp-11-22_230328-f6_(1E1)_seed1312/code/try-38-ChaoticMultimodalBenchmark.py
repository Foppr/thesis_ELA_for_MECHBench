import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with fractional Brownian motion-like behavior
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.3 * np.sin(15 * r) * np.cos(7 * r))
        
        # Sinusoidal coupling between dimensions with varying frequencies
        sin_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sin_coupling += np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Chaotic component using a modified logistic map interaction
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(8 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i]) * np.sin(4 * np.pi * x_norm[(i+1) % self.dim])
        
        # Multi-scale trigonometric modulation
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += (np.sin(20 * x_norm[i]) + 0.5 * np.cos(30 * x_norm[i])) * np.exp(-0.5 * (x_norm[i]**2))
        
        # Adaptive scaling based on dimensionality and position
        adaptive_scale = 1.0 + 0.2 * np.sin(2 * r) * np.cos(3 * r) * self.dim
        
        # Cross-dimensional interaction with fractal-like behavior
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.abs(x_norm[i] - x_norm[j])**0.7) * np.exp(-np.abs(x_norm[i] + x_norm[j]))
        
        # Add a global periodic modulation
        global_mod = 0.1 * np.sin(2 * np.pi * r) * np.cos(3 * np.pi * r)
        
        return adaptive_scale * (radial_term + sin_coupling + chaotic_term + trig_term + cross_term + global_mod)