import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # Highly oscillatory sinusoidal terms with exponential scaling
        sinusoidal = np.sum(np.exp(2 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm)**2)
        
        # Polynomial interaction terms
        polynomial = np.sum((x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2) * np.cos(3 * np.pi * x_norm))
        
        # Cross-dimensional interaction using exponential decay
        cross_term = np.exp(-np.sum(np.abs(x_norm))) * np.prod(np.sin(2 * np.pi * x_norm))
        
        # Add a global minimum perturbation
        perturbation = 0.01 * np.sum(np.sin(15 * x_norm)**4)
        
        # Combine all terms with varying weights
        return 2.0 * quadratic + 0.5 * sinusoidal + 0.2 * polynomial + 0.05 * cross_term + perturbation