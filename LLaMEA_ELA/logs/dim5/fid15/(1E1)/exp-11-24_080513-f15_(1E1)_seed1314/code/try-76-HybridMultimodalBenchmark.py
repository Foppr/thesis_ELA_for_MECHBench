import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Periodic component with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            periodic += np.sin(freq * np.pi * x_normalized[i])**2 + np.cos(freq * np.pi * x_normalized[i])**2
        
        # Exponential decay with adaptive scaling
        exponential = 0.0
        for i in range(self.dim):
            scale = 0.5 + 0.5 * np.sin(i * 0.7)
            exponential += scale * np.exp(-0.5 * x_normalized[i]**2) * (1 + 0.3 * np.sin(3 * x_normalized[i]))
        
        # Saddle-point components with varying curvature
        saddle = 0.0
        for i in range(self.dim):
            curvature = 1.0 + 0.5 * np.cos(i * 0.5)
            saddle += curvature * x_normalized[i]**2 * (1 - x_normalized[i]**2)
        
        # Cross-dimensional coupling with adaptive weights
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                weight = 0.3 + 0.7 * np.sin((i+j) * 0.3)
                cross += weight * np.sin(2 * (x_normalized[i] + x_normalized[j])) * \
                         (x_normalized[i]**2 + x_normalized[j]**2) * \
                         np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Adaptive noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(5 * x_normalized[i]) * np.cos(7 * x_normalized[i]) * \
                     np.exp(-0.1 * x_normalized[i]**2) * (1 + 0.2 * np.random.random())
        
        # Dimensionality-dependent scaling
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components with adaptive weights
        return (0.3 * periodic + 0.4 * exponential + 0.2 * saddle + 
                0.05 * cross + 0.05 * noise) * dim_factor