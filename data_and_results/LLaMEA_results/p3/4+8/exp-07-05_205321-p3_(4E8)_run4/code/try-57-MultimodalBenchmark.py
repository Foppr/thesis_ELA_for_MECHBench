import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial fractal-like component with multiple frequency harmonics
        r = np.sqrt(np.sum(x_scaled**2))
        fractal = np.sum(np.sin(2**np.arange(1, self.dim + 1) * np.pi * r) * 
                         np.cos(3**np.arange(1, self.dim + 1) * np.pi * r))
        
        # Multi-scale sinusoidal interference with dynamic amplitude
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interference += np.sin(10 * np.pi * dist) * np.cos(5 * np.pi * dist) * (1.0 + 0.1 * dist)
        
        # Gradient complexity with polynomial and exponential interactions
        grad_complexity = np.sum(x_scaled**4 + 0.5 * np.exp(-x_scaled**2) + 
                                0.3 * np.sin(8 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Saddle point enhancement with cross-dimensional interactions
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x_scaled[i]**2 - x_scaled[i+1]**2) * (x_scaled[i] + x_scaled[i+1])**2
        
        # Dynamic scaling based on dimensionality
        scaling = np.sum((1.0 + 0.1 * np.sin(20 * np.pi * x_scaled)) * x_scaled**2)
        
        # High-frequency chaotic modulation
        chaotic_mod = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) * 
                            np.sin(9 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Combine all components with appropriate weights
        return 0.2 * fractal + 0.3 * interference + 0.15 * grad_complexity + 0.15 * saddle + 0.1 * scaling + 0.1 * chaotic_mod + 2.5