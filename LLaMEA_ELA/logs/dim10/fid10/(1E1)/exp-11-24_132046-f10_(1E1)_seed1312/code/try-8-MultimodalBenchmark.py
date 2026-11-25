import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic oscillation with non-linear frequency modulation
        f2 = 0.5 * np.sum(np.sin(10 * np.pi * x_norm * np.exp(-0.5 * x_norm**2)) * 
                          np.cos(7 * np.pi * x_norm * np.exp(-0.3 * x_norm**2)))
        
        # Asymmetric saddle points with varying depths
        f3 = 0.3 * np.sum(np.exp(-x_norm**2) * np.sin(3 * np.pi * x_norm) * 
                          np.cos(4 * np.pi * x_norm))
        
        # Conditional interaction with exponential activation
        f4 = 0.2 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                          (x_norm[:-1]**3 + x_norm[1:]**3))
        
        # Fourth-order polynomial with random coefficients for increased curvature
        coeffs = np.random.uniform(0.1, 0.5, self.dim)
        f5 = np.sum(coeffs * x_norm**4)
        
        # Cross-dimensional coupling with logarithmic scaling
        f6 = 0.15 * np.sum(np.log(1 + np.abs(x_norm[:-1] - x_norm[1:])) * 
                           (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add a chaotic component that depends on all dimensions
        f7 = 0.1 * np.sum(np.sin(np.pi * np.sum(x_norm**3, axis=0)) * 
                          np.cos(2 * np.pi * np.sum(x_norm**2, axis=0)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7