import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = x / 5.0
        
        # Periodic oscillatory components with varying frequencies
        oscillation1 = np.sum(np.sin(2 * np.pi * x) ** 2)
        oscillation2 = np.sum(np.cos(3 * np.pi * x) ** 2)
        oscillation3 = np.sum(np.sin(5 * np.pi * x) ** 2)
        
        # Asymmetric saddle point structure
        saddle = np.sum(x ** 2 * np.exp(-x ** 2))
        
        # Nested local minima with varying depths
        nested = 0.0
        for i in range(self.dim):
            nested += (x[i] ** 4 - 10 * x[i] ** 2 + 5 * x[i]) * np.cos(2 * np.pi * x[i])
        
        # Directional bias with anisotropic scaling
        anisotropic = 0.0
        for i in range(self.dim):
            anisotropic += (i + 1) * x[i] ** 3
        
        # Combine all components
        result = oscillation1 + oscillation2 + oscillation3 + saddle + nested + anisotropic
        
        # Add a small noise term to increase robustness testing
        noise = 0.001 * np.sum(np.random.randn(self.dim) * x)
        result += noise
        
        return result