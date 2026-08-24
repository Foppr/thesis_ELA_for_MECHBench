import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic basin term for global minimum attraction
        quadratic = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with exponential decay
        sinusoidal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            sinusoidal += np.sum(np.sin(i * np.pi * x_normalized) * np.exp(-i * np.abs(x_normalized)))
        
        # Polynomial barrier terms to create complex local optima
        barrier = 0.0
        for i in range(self.dim):
            barrier += 0.5 * (x_normalized[i]**6 - 3 * x_normalized[i]**4 + 2 * x_normalized[i]**2)
        
        # Cross-term interaction to increase dimensionality complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(x_normalized[i]) * np.cos(x_normalized[j])
        
        # Additional penalty term for convergence to origin
        penalty = 0.2 * np.sum(np.abs(x_normalized)**3)
        
        return quadratic + sinusoidal + barrier + cross_term + penalty