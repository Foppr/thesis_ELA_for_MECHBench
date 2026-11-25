import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_normalized**2)
        
        # Highly oscillatory sinusoidal terms with exponentially increasing frequencies
        sinusoidal = np.sum(np.sin(np.pi * np.power(2.0, np.arange(1, self.dim + 1)) * x_normalized))
        
        # Polynomial barrier terms to create rugged terrain
        barriers = np.sum(np.power(np.abs(x_normalized), 3.0 + np.arange(self.dim)))
        
        # Exponentially weighted penalty for large values
        penalty = np.sum(np.exp(2.0 * np.abs(x_normalized)) - 1.0)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components with adaptive scaling
        return condition_factor * (quadratic + sinusoidal + barriers + penalty)