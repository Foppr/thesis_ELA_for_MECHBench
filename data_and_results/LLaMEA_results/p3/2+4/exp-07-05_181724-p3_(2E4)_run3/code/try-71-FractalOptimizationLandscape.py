import numpy as np

class FractalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like self-similar structure using recursive sine components
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            fractal += np.sum(np.sin(2**(i) * np.pi * x_norm)**2)
        
        # Logarithmic barrier terms to create narrow passages
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1.0 + 0.1 * np.abs(x_norm[i]))
        
        # Saddle-point structure with mixed polynomial and trigonometric terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**4 - 2 * x_norm[i]**2
        
        # Multi-scale oscillatory component
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
        
        # Coupled cubic interactions between dimensions
        coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += (x_norm[i] * x_norm[i+1])**3
        
        # Gaussian-like ridges with varying widths
        ridge = 0.0
        for i in range(self.dim):
            ridge += np.exp(-0.5 * (x_norm[i] - 0.5)**2) + np.exp(-0.5 * (x_norm[i] + 0.5)**2)
        
        # Add a small random perturbation for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.2 * quadratic + 
                0.3 * fractal + 
                0.1 * log_barrier + 
                0.15 * saddle + 
                0.1 * oscillatory + 
                0.1 * coupling + 
                0.05 * ridge + 
                noise)