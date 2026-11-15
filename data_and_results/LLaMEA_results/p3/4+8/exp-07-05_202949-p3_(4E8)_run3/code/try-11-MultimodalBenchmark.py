import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal perturbations with exponential decay
        f2 = np.sum(np.sin(10.0 * x) * np.exp(-0.5 * np.abs(x)))
        
        # Additional multimodal component with multiple peaks
        f3 = 0.5 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.exp(-0.2 * x**2))
        
        # Long-range attractive forces to guide convergence
        f4 = 0.1 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(2.0 * x))
        
        # Add a complex interaction term between dimensions
        interaction = 0.05 * np.sum((x[:-1] - x[1:]) ** 2 * np.exp(-0.05 * (x[:-1] + x[1:]) ** 2))
        
        return f1 + f2 + f3 + f4 + interaction