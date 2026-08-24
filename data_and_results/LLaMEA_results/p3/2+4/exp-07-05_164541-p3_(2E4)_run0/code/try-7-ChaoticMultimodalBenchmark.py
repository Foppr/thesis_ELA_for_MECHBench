import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Chaotic component with exponential decay and trigonometric oscillations
        chaotic = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Additional higher-order terms for increased complexity
        high_order = 0.01 * np.sum(np.abs(x)**3)
        
        # Combine all components
        result = quadratic + chaotic + high_order
        
        return result