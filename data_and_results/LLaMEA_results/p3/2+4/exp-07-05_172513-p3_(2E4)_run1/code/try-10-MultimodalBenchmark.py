import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic term for global convergence
        quadratic = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms creating many local minima
        sinusoidal = np.sum(np.sin(10 * np.pi * x_normalized) ** 2)
        
        # Exponentially increasing barrier terms to create deep local optima
        barrier = np.sum(np.exp(2 * np.abs(x_normalized)) - 1)
        
        # Coupling between dimensions to increase complexity
        coupling = np.sum(np.sin(np.pi * x_normalized[0] * x_normalized[1]) ** 2)
        
        # Adaptive penalty that increases with distance from origin
        penalty = 0.5 * np.sum((x_normalized**4) * (1 + np.abs(x_normalized)))
        
        return quadratic + 2 * sinusoidal + 0.5 * barrier + 0.1 * coupling + penalty