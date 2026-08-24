import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with exponential decay and amplitude modulation
        frequencies = np.arange(1, self.dim + 1)
        sinusoidal = np.sum(np.sin(frequencies * np.pi * x_normalized) * np.exp(-0.15 * frequencies) * (1 + 0.5 * np.cos(2 * frequencies * x_normalized)))
        
        # Polynomial correlation terms of increasing degree
        polynomial = 0.0
        for i in range(1, 7):
            polynomial += np.sum(x_normalized**i) * (0.12 / i)
        
        # Mixed exponential and trigonometric interactions with additional phase shift
        interaction = np.sum(np.exp(-x_normalized**2) * np.cos(12 * x_normalized + np.pi/4))
        
        # Shifted global minimum to increase challenge
        shift = 0.3
        return quadratic + 0.6 * sinusoidal + 0.06 * polynomial + 0.12 * interaction + 1.0 + shift * np.sum((x_normalized - 0.2)**2)