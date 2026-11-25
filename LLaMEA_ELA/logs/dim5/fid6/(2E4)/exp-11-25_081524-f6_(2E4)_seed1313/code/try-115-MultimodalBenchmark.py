import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(2.0 * np.pi * x[i] / (1.0 + 0.2 * i)) * np.cos(3.0 * x[i])
        
        # Radial basis function with adaptive width
        rbf_term = 0.0
        for i in range(self.dim):
            dist = np.sum((x - x[i])**2)
            width = 1.0 + 0.3 * np.abs(x[i])
            rbf_term += np.exp(-0.5 * dist / width)
        
        # Asymmetric saddle point structure with exponential decay
        saddle_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            saddle_term += diff**2 * np.exp(-0.15 * np.abs(diff)) * (1.0 + 0.4 * np.sin(x[i]))
        
        # Cross-dimensional interaction with polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim-2):
            poly_coupling += (x[i] * x[i+1] * x[i+2])**2.5
        
        # Global scaling and noise modulation
        scale_factor = 1.0 + 0.3 * np.sin(0.6 * self.dim)
        
        return (sin_term + rbf_term + saddle_term + poly_coupling) * scale_factor