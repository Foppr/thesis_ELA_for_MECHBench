import numpy as np

class ChaoticAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic component with multiple frequencies
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Saddle point structure with asymmetric quadratic terms
        for i in range(self.dim):
            f += 0.5 * x[i]**2 - 0.3 * x[i]**3 + 0.1 * x[i]**4
            
        # Multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.3 * np.sin(10 * x[i]) + 0.2 * np.cos(15 * x[i]) + 0.1 * np.sin(20 * x[i])
            
        # Exponential scaling and bias to create varied landscape curvature
        for i in range(self.dim):
            f += 0.2 * np.exp(-0.5 * x[i]**2) * np.sin(7 * x[i])
            
        # Fractal-like structure with recursive harmonic components
        for i in range(self.dim):
            f += 0.1 * np.sin(23 * x_norm[i]) * np.cos(29 * x_norm[i]) * np.sin(31 * x_norm[i])
            
        # Chaotic modulation with dynamic weights
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(37 * x_norm[i]) * np.cos(41 * x_norm[i]) * np.sin(43 * x_norm[i]) * np.cos(47 * x_norm[i])
        f += 0.15 * chaos
        
        # Additional coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1 + 0.1 * np.sin(i + j))
                
        # Global minimum attraction with polynomial terms
        f += 0.2 * np.sum(x**6) + 0.1 * np.sum(x**8)
        
        # Final scaling to ensure proper fitness range
        f *= 1.0 + 0.05 * np.sum(np.abs(x))
        
        return f