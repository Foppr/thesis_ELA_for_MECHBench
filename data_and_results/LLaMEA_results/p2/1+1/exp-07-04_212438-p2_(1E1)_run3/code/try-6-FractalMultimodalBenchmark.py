import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Fractal-like component with recursive sine and cosine
        f2 = np.sum(np.sin(10.0 * np.sin(5.0 * x)) * np.cos(3.0 * x))
        
        # Multi-scale oscillation component
        f3 = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.sin(8.0 * x))
        
        # Recursive fractal term with exponential decay
        f4 = np.sum(np.sin(np.pi * np.sin(np.pi * x)) * np.exp(-0.5 * x**2))
        
        # High-frequency noise component
        f5 = np.sum(np.sin(50.0 * x) * np.cos(30.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all components with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.05 * f5