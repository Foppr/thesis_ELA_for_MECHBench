import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Exponential decay terms with chaotic frequencies
        for i in range(self.dim):
            f += 0.5 * np.exp(-0.1 * x[i]**2) * np.sin(10 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            
        # Trigonometric coupling with varying phase shifts
        for i in range(self.dim):
            f += 0.3 * np.sin(5 * x[i] + 0.5 * x[(i + 2) % self.dim]) * np.cos(3 * x[(i + 1) % self.dim] + 0.3 * x[(i + 3) % self.dim])
            
        # Polynomial ridge structure with chaotic modulation
        ridge_term = 0
        for i in range(self.dim):
            ridge_term += (x[i] - 0.5 * x[(i + 1) % self.dim])**2
        f += 0.4 * ridge_term**1.5
        
        # Cross-dimensional polynomial interactions with exponential weights
        for i in range(self.dim):
            f += 0.2 * np.exp(-0.05 * np.abs(x[i])) * x[i]**3 * x[(i + 2) % self.dim]**2
            
        # Chaotic oscillatory penalty terms
        for i in range(self.dim):
            f += 0.15 * np.sin(12 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim])
            
        # Additional ridge-like structure with varying curvature
        for i in range(self.dim):
            f += 0.25 * (x[i]**2 + x[(i + 1) % self.dim]**2)**1.8
            
        # High-frequency chaotic modulation
        for i in range(self.dim):
            f += 0.3 * np.sin(20 * x[i]) * np.cos(15 * x[(i + 1) % self.dim]) * np.sin(11 * x[(i + 2) % self.dim])
            
        # Asymmetric penalty for large deviations
        f += 0.3 * np.sum(np.abs(x)**4.2) + 0.1 * np.sum(x**6)
        
        return f