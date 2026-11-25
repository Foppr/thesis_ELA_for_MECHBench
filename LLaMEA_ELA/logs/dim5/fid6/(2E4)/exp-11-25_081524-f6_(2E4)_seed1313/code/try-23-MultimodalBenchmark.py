import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponentially weighted sinusoidal terms with varying frequencies
        exp_sinusoidal = np.sum(np.exp(0.5 * np.abs(x)) * np.sin(3.0 * x)) + \
                         0.3 * np.sum(np.exp(0.3 * np.abs(x)) * np.cos(4.0 * x))
        
        # Cubic cross-terms creating complex interaction patterns
        cubic_cross = 0.2 * np.sum((x[:-2] * x[1:-1] * x[2:])**3)
        
        # Polynomial with mixed degrees to create varied curvature
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**3) + 0.01 * np.sum(x**6)
        
        # Valley structure with asymmetric basins
        valley = np.sum((x - np.sin(x))**2) + 0.5 * np.sum(np.abs(x[:-1] - x[1:])**3)
        
        return polynomial + exp_sinusoidal + cubic_cross + valley