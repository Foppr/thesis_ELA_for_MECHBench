import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with increasing degree
        polynomial = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Exponential decay terms with varying rates
        exponential = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Trigonometric components with varying frequencies
        trigonometric = np.sum(np.cos(2 * np.pi * x_norm) + 0.5 * np.sin(3 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * (self.dim - 1)
        
        # Combine all components with conditioning
        result = condition_factor * (polynomial + exponential + trigonometric)
        
        # Add small random perturbation for landscape complexity
        noise = 0.01 * np.random.random()
        
        return result + noise