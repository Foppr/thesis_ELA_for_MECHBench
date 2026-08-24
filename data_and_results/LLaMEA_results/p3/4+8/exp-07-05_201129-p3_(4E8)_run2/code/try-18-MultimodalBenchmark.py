import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with exponential decay
        frequencies = np.arange(1, self.dim + 1)
        sinusoidal = np.sum(np.sin(frequencies * np.pi * x_normalized) * np.exp(-0.1 * frequencies))
        
        # Polynomial correlation terms of increasing degree
        polynomial = 0.0
        for i in range(1, 6):
            polynomial += np.sum(x_normalized**i) * (0.1 / i)
        
        # Mixed exponential and trigonometric interactions
        interaction = np.sum(np.exp(-x_normalized**2) * np.cos(10 * x_normalized))
        
        # Global minimum at origin with additional local minima
        return quadratic + 0.5 * sinusoidal + 0.05 * polynomial + 0.1 * interaction + 1.0