import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic component with multiple frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += (np.sin(2 * np.pi * x[i]) + 
                        0.5 * np.sin(4 * np.pi * x[i]) + 
                        0.3 * np.sin(8 * np.pi * x[i]))
        
        # Exponential decay component with varying rates
        exponential = 0
        for i in range(self.dim):
            exponential += (np.exp(-0.1 * np.abs(x[i])) * 
                           np.cos(0.5 * x[i]) + 
                           np.exp(-0.2 * np.abs(x[i])) * 
                           np.sin(0.3 * x[i]))
        
        # Radial basis function component with adaptive scaling
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                rbf += np.exp(-0.5 * ((x[i] - centers[i]) / (1.0 + 0.1 * np.abs(x[i])))**2)
        
        # Adaptive conditioning component with dimension-dependent scaling
        conditioning = 0
        for i in range(self.dim):
            conditioning += (x[i]**2 * (1 + 0.1 * np.sin(5 * x[i])) + 
                           x[i]**4 * (1 + 0.05 * np.cos(3 * x[i])))
        
        # Cross-dimensional interaction terms
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction for scalability
                interaction += (np.sin(x[i] - x[j]) * np.cos(x[i] + x[j]) * 
                               np.exp(-0.1 * (x[i]**2 + x[j]**2)))
        
        # Combine components with dynamic weights based on dimensionality
        weight_periodic = 0.3 * (1 + 0.1 * self.dim)
        weight_exponential = 0.25 * (1 + 0.05 * self.dim)
        weight_rbf = 0.2 * (1 + 0.02 * self.dim)
        weight_conditioning = 0.15 * (1 + 0.03 * self.dim)
        weight_interaction = 0.1 * (1 + 0.01 * self.dim)
        
        return (weight_periodic * periodic + 
                weight_exponential * exponential + 
                weight_rbf * rbf + 
                weight_conditioning * conditioning + 
                weight_interaction * interaction)