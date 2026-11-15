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
        sinusoidal = np.sum(np.sin(frequencies * np.pi * x_normalized) * np.exp(-0.15 * frequencies))
        
        # Polynomial correlation terms of increasing degree with modified coefficients
        polynomial = 0.0
        for i in range(1, 7):
            polynomial += np.sum(x_normalized**i) * (0.15 / i)
        
        # Mixed exponential and trigonometric interactions with altered weights
        interaction = np.sum(np.exp(-0.5 * x_normalized**2) * np.cos(15 * x_normalized))
        
        # Shifted global minimum and additional local optima
        return quadratic + 0.6 * sinusoidal + 0.07 * polynomial + 0.15 * interaction + 1.5