import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sinusoidal modulations with varying frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10 * x[i] + np.sin(3 * x[i])) * np.cos(7 * x[i] + np.cos(2 * x[i]))
        
        # Radial basis function components with random centers and varying widths
        rbf_term = 0.0
        for i in range(self.dim):
            center = np.sin(i) * 4.0
            width = 0.5 + 0.5 * np.cos(i)
            rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_term += np.exp(-0.1 * diff**2) * np.sin(5 * diff)
        
        # Multi-scale periodic structure with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += 0.6 * np.sin(15 * x[i]) * np.cos(9 * x[i]) * np.sin(3 * x[i])
        
        # Add a global conditioning factor based on the norm
        condition_factor = 1.0 + 0.2 * np.sum(np.abs(x_norm))
        
        # Combine all terms
        result = condition_factor * (quadratic + chaotic_term + rbf_term + cross_term + multi_scale)
        
        return result