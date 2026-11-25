import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying centers and widths
        centers = np.linspace(-4.5, 4.5, min(10, self.dim))
        widths = np.logspace(-1, 1, min(10, self.dim))
        rbf = np.sum([np.exp(-widths[i] * (x - centers[i])**2) for i in range(min(10, self.dim))])
        
        # Sinusoidal oscillation with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x * (1 + 0.1 * np.sin(x))) * 
                         np.cos(3 * np.pi * x * (1 + 0.05 * np.cos(x))))
        
        # Chaotic perturbation using logistic map for non-linearity
        chaotic_pert = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_pert += np.sin(10 * (x[i] + x[i+1]) * 
                                     np.exp(-0.5 * (x[i]**2 + x[i+1]**2)))
        
        # Polynomial interaction with noise
        poly_term = np.sum((x**3 - 2 * x**2 + x) * 
                          (1 + 0.1 * np.random.randn(self.dim)))
        
        # Add a global minimum at the origin with additional chaotic modulation
        global_min = np.sum(x**2 * np.exp(-0.1 * np.sum(x**2)))
        
        return rbf + sin_term + chaotic_pert + poly_term + global_min