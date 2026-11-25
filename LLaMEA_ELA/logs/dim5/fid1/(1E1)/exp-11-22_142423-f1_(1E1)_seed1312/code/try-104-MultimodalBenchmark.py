import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add periodic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.7 * np.sin(10 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) + 0.5 * np.sin(5 * x[i]) * np.cos(3 * x[(i + 2) % self.dim])
            
        # Introduce asymmetric saddle points with non-uniform exponents
        for i in range(self.dim):
            f += 0.3 * (x[i]**4 - 2 * x[i]**2 + 1) * np.cos(2 * x[(i + 1) % self.dim])
            
        # Add cross-dimensional coupling with varying phase shifts and interaction strengths
        for i in range(self.dim):
            f += 0.2 * np.sin(3 * x[i]) * np.cos(4 * x[(i + 3) % self.dim]) * np.sin(2 * x[(i + 5) % self.dim])
            
        # Incorporate non-separable higher-order terms
        for i in range(self.dim):
            f += 0.15 * x[i]**3 * x[(i + 1) % self.dim]**2 + 0.1 * x[i]**2 * x[(i + 2) % self.dim]**3
            
        # Add chaotic perturbations using logistic map-like behavior
        for i in range(self.dim):
            f += 0.25 * np.sin(8 * x[i] + np.sin(5 * x[(i + 1) % self.dim])) * np.cos(6 * x[(i + 2) % self.dim])
            
        # Include irregular penalty terms to increase difficulty
        f += 0.3 * np.sum(np.abs(x)**2.5) + 0.1 * np.sum(x**4)
        
        return f