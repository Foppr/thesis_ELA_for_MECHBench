import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**3) + 0.01 * np.sum(x**4)
        
        # Trigonometric components with coupled interactions
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trigonometric += np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) + \
                                np.cos(4.0 * x[i]) * np.sin(5.0 * x[j])
        
        # Radial basis function component with multiple centers
        rbfs = 0.0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for center in centers:
            if len(centers) <= self.dim:
                rbfs += np.exp(-0.5 * np.sum((x - center)**2))
        
        # Correlation term between dimensions
        correlation = 0.0
        for i in range(self.dim - 1):
            correlation += (x[i] - x[i+1])**2 * np.sin(3.0 * x[i])
        
        # Adaptive scaling factor
        adaptive_scale = 1.0 + 0.05 * np.log(self.dim + 1)
        
        return adaptive_scale * (polynomial + 0.2 * trigonometric + 0.1 * rbfs + 0.05 * correlation)