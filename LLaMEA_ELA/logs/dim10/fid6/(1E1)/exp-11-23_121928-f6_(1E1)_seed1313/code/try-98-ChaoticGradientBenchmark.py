import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        base = np.sum(x_norm**2)
        
        # Chaotic sine-modulated gradient terms
        chaotic_terms = np.zeros_like(x_norm)
        for i in range(self.dim):
            chaotic_terms[i] = np.sin(13 * x_norm[i]) * np.cos(7 * x_norm[i]**3) * np.exp(-0.5 * x_norm[i]**2)
        
        # Periodic attractor landscape with adaptive frequency
        attractor = np.sum(np.sin(2 * np.pi * (x_norm + 0.1 * np.sin(5 * x_norm)))**2)
        
        # Multi-scale curvature modulation
        curvature = np.sum((x_norm**4) * np.cos(3 * x_norm) * np.sin(2 * x_norm))
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Coupled oscillatory interaction
        coupling = np.sum(np.sin(x_norm * (1 + 0.3 * np.cos(4 * x_norm))) * np.cos(x_norm * (1 + 0.2 * np.sin(3 * x_norm))))
        
        # Fractional power landscape with singularity
        fractional = np.sum(np.abs(x_norm)**1.7 * np.sin(5 * x_norm))
        
        # Combined function with competing forces
        result = adaptive_scale * (0.4 * base + 0.3 * np.sum(chaotic_terms) + 0.2 * attractor + 
                                  0.1 * curvature + 0.05 * coupling + 0.05 * fractional)
        
        # Add small noise to prevent exact replication
        result += 0.001 * np.random.rand()
        
        return result