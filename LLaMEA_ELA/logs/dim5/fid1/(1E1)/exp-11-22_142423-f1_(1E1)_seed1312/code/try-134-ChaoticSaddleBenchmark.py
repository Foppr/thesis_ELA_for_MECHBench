import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add periodic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim]) + 0.3 * np.sin(4 * x[i]) * np.cos(5 * x[(i + 2) % self.dim])
            
        # Introduce asymmetric saddle points using cubic and quartic terms
        for i in range(self.dim):
            f += 0.1 * x[i]**3 * np.sin(x[(i + 1) % self.dim]) + 0.05 * x[i]**4
            
        # Add adaptive cross-dimensional coupling with dimension-dependent weights
        weight_factor = 0.2 + 0.1 * np.sin(self.dim)
        for i in range(self.dim):
            f += weight_factor * np.cos(2 * x[i]) * np.sin(3 * x[(i + 3) % self.dim]) * x[i]**2
            
        # Include non-uniform penalty terms to increase difficulty near boundaries
        f += 0.15 * np.sum(np.abs(x)**2.5) + 0.1 * np.sum(np.abs(x)**4)
        
        # Add chaotic interaction through higher-order polynomials and trigonometric mixtures
        for i in range(self.dim):
            f += 0.08 * np.sin(7 * x[i]) * np.cos(6 * x[(i + 2) % self.dim]) * x[(i + 1) % self.dim]**3
            
        # Incorporate shifted local minima with varying depths
        for i in range(self.dim):
            f += 0.25 * (np.sin(x[i] - 1.5)**2 + np.cos(x[(i + 1) % self.dim] + 1.0)**2)
            
        return f