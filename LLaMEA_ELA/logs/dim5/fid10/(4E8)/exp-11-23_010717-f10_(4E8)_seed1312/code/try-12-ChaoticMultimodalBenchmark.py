import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (1.0 + 0.5 * np.sin(10 * r))
        
        # Angular components with multiple frequencies
        angles = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0.0
        angular = np.sum(np.sin((np.arange(1, self.dim + 1) + 1) * angles)) if self.dim > 1 else 0.0
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Quadratic penalty term
        quadratic = np.sum(x_norm**2)
        
        # Combine all components with varying weights
        return 0.3 * radial + 0.4 * angular + 0.2 * chaotic + 0.1 * quadratic