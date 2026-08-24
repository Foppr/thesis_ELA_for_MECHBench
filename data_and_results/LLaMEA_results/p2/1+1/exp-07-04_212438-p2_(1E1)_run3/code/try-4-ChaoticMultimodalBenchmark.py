import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Exponential decay with sinusoidal modulation (modified decay rate)
        f2 = np.sum(np.exp(-0.3 * x**2) * np.sin(3.0 * x))
        
        # Chaotic component using logistic map-like behavior with cosine modulation
        f3 = np.sum(np.sin(x) * np.cos(2.0 * x) * np.exp(-0.15 * np.abs(x)) * np.cos(5.0 * x))
        
        # Add a term that creates ruggedness through high-frequency oscillations
        f4 = 0.5 * np.sum(np.sin(20.0 * x) * np.exp(-0.02 * x**2))
        
        # Combine all components with different weights
        return f1 + 0.35 * f2 + 0.25 * f3 + 0.15 * f4