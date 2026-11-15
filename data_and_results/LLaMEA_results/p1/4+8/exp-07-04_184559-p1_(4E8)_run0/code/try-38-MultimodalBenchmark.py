import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal modulation with multiple frequencies
        f2 = np.sum(np.sin(10 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm)**2)
        
        # Radial bias term to create complex landscape
        radius = np.sqrt(np.sum(x_norm**2))
        f3 = 0.5 * radius * np.sin(3 * np.pi * radius)**2
        
        # Additional harmonic term with adaptive scaling
        f4 = 0.1 * np.sum((x_norm - 0.3)**2 * (1 + 0.5 * np.sin(8 * np.pi * x_norm)))
        
        # Combine terms to create a challenging landscape
        return f1 + 0.8 * f2 + 0.3 * f3 + 0.2 * f4