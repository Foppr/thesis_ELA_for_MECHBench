import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term for global minimum attraction
        quadratic = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with exponential growth
        sinusoidal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            sinusoidal += np.sum(np.sin((2**i) * np.pi * x_normalized)**2)
        
        # Polynomial penalty with higher order terms
        penalty = 0.1 * np.sum(np.abs(x_normalized)**4)
        
        # Cross-dimensional interaction terms to increase complexity
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_normalized[i] * x_normalized[j])**2
        
        # Add a small noise component to make the landscape less predictable
        noise = 0.01 * np.sum(np.sin(100 * x_normalized)**2)
        
        return quadratic + sinusoidal + penalty + interaction + noise