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
        f2 = np.sum(np.sin(12.0 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Additional complex multimodal component with multiple local minima
        f3 = 0.5 * np.sum(np.sin(4.0 * x) * np.cos(8.0 * x) * np.exp(-0.1 * x**2))
        
        # Add a global minimum at origin with a non-convex penalty
        f4 = 0.03 * np.sum(np.abs(x)**3)
        
        # Add a long-range interaction term to increase complexity
        f5 = 0.15 * np.sum(np.sin(0.3 * x) * np.exp(-0.03 * np.sum(x**2)))
        
        # Add cubic interaction terms for increased complexity
        f6 = 0.02 * np.sum(x**3 * np.sin(2.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6