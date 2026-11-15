import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal perturbations with exponential decay
        f2 = np.sum(np.sin(10.0 * x) * np.exp(-0.5 * np.abs(x)))
        
        # Additional complex multimodal component with multiple local minima
        f3 = 0.5 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.exp(-0.2 * x**2))
        
        # Add a global minimum at origin with a non-convex penalty
        f4 = 0.05 * np.sum(np.abs(x)**4)
        
        # Add a long-range interaction term to increase complexity
        f5 = 0.1 * np.sum(np.sin(0.5 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5