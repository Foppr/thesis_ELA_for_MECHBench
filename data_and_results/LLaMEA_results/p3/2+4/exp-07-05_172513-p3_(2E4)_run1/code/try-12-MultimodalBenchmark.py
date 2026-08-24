import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic term for conditioning and global minimum
        quadratic = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with different frequencies for increased complexity
        sinusoidal = np.sum(np.sin(3 * np.pi * x_normalized) ** 2) + \
                     np.sum(np.sin(7 * np.pi * x_normalized) ** 2) + \
                     np.sum(np.sin(11 * np.pi * x_normalized) ** 2)
        
        # Radial basis function component to create multiple local minima
        radial = np.sum(np.exp(-5.0 * np.sum(x_normalized**2)))
        
        # Cross-term interaction to increase problem difficulty
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Additional penalty term to discourage large values
        penalty = 0.05 * np.sum(np.abs(x_normalized)**3)
        
        return quadratic + sinusoidal + radial + cross_term + penalty