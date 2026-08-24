import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic forcing coefficients
        self.coeffs = np.array([np.sin(i * np.pi / 4) for i in range(dim)])
    
    def f(self, x):
        # Clip input to domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quad = 0.5 * np.sum(x**2)
        
        # Chaotic gradient component with periodic forcing
        grad = 0
        for i in range(self.dim):
            grad += (x[i]**3 + 0.5 * x[i]**2 + 0.1 * x[i]) * self.coeffs[i]
        
        # Saddle-point clustering with exponential decay
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                saddle += np.exp(-dist**2) * np.sin(10 * dist) * (x[i]**2 + x[j]**2)
        
        # Implicit constraint penalty (nonlinear)
        penalty = 0
        for i in range(self.dim):
            penalty += (np.sin(x[i]) - 0.5 * np.cos(2 * x[i]))**2
        
        # Periodic forcing modulation
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(2 * np.pi * x[i] / 5.0) * np.cos(3 * np.pi * x[i] / 5.0)
        
        # Combined function value
        return quad + 0.3 * grad + 0.2 * saddle + 0.1 * penalty + 0.05 * periodic