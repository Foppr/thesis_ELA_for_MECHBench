import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin to encourage convergence to origin
        quadratic = np.sum(x_normalized**2)
        
        # Sinusoidal terms with exponentially increasing frequency
        sinusoidal = 0.0
        for i in range(1, self.dim + 1):
            sinusoidal += np.sin(i * np.pi * x_normalized) ** 2 * np.exp(-0.1 * i)
        
        # Additional ruggedness via Gaussian noise modulation
        ruggedness = np.sum(np.exp(-10 * (x_normalized - 0.5)**2) + np.exp(-10 * (x_normalized + 0.5)**2))
        
        # Combine all components
        return quadratic + sinusoidal + ruggedness