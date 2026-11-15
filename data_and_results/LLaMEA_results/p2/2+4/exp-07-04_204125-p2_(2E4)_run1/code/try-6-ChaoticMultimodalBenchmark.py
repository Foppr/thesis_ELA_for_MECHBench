import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f1 = np.sum(x**2)
        
        # Add chaotic component with exponential decay
        f2 = 0.5 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x))
        
        # Add a highly oscillatory term with varying frequency
        f3 = 0.3 * np.sum(np.sin(20.0 * x) * np.cos(5.0 * x) * np.exp(-0.05 * x**2))
        
        # Introduce a discontinuous element to increase complexity
        f4 = 0.2 * np.sum(np.abs(x) * np.sin(15.0 * x))
        
        # Combine all components
        return f1 + f2 + f3 + f4