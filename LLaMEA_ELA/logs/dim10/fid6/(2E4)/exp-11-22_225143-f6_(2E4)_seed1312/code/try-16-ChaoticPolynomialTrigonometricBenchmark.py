import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base polynomial term with conditioning
        f_val = np.sum(x_norm**4) * (1.0 + 0.2 * np.sum(np.abs(x_norm)))
        
        # Add chaotic trigonometric interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 1.5 * np.sin(3 * x_norm[i])**3 * np.cos(7 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Add long-range dependencies with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Limited but extended interaction
                distance = np.abs(x_norm[i] - x_norm[j])
                f_val += 0.5 * np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(3 * np.pi * (x_norm[i] - x_norm[j])) * np.exp(-distance**2)
        
        # Add saddle point structure with mixed polynomial and trigonometric terms
        for i in range(self.dim):
            f_val += 0.3 * (x_norm[i]**6 - 2 * x_norm[i]**4 + x_norm[i]**2) * np.cos(5 * np.pi * x_norm[i])
        
        # Add global structure with multiple competing optima
        f_val += 0.4 * np.sum(np.sin(4 * np.pi * x_norm)**2 + np.cos(3 * np.pi * x_norm)**2)
        
        # Add chaotic perturbation with cubic interactions
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += (np.sin(5 * x_norm[i])**3) * (np.cos(4 * x_norm[i])**2) * (np.sin(3 * x_norm[i]) + 0.1)
        f_val += 0.3 * chaos_term
        
        # Add cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.25 * np.exp(-2 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(6 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        return f_val