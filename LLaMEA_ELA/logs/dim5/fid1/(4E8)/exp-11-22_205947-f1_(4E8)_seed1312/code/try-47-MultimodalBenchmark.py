import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with multiple roots
        poly_term = np.sum(x_norm**6) + 0.5 * np.sum(x_norm**4)
        
        # Trigonometric terms with chaotic tent map modulation
        trig_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation using tent map dynamics
            tent_map = 1.0 - 2.0 * np.abs(x_norm[i])
            trig_term += (np.sin(12 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i]) + 
                         np.sin(5 * np.pi * x_norm[i])**2 * np.cos(3 * np.pi * x_norm[i])) * tent_map
            
        # Radial basis function component with asymmetric centers
        rbf_term = 0.0
        centers = np.linspace(-0.8, 0.8, self.dim)
        for i in range(self.dim):
            rbf_term += np.exp(-5.0 * (x_norm[i] - centers[i])**2) + \
                       0.3 * np.exp(-3.0 * (x_norm[i] + centers[i])**2)
        
        # Cross-dimensional coupling with varying interaction strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                strength = 0.5 * (1 + np.sin(np.pi * (i + j) / self.dim))
                cross_term += strength * np.sin(6 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        # Asymmetric penalty term
        asym_term = 0.0
        for i in range(self.dim):
            asym_term += (x_norm[i] - 0.2)**4 + 0.5 * (x_norm[i] + 0.3)**3
        
        # Combine all terms with different weights
        result = 0.8 * poly_term + 0.6 * trig_term + 0.4 * rbf_term + 0.2 * cross_term + 0.3 * asym_term
        
        return result