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
        
        # Enhanced exponential decay with sinusoidal modulation
        f2 = np.sum(np.exp(-0.4 * x**2) * np.sin(4.0 * x))
        
        # Chaotic component using sine-cosine product with modified decay
        f3 = np.sum(np.sin(x) * np.cos(3.0 * x) * np.exp(-0.2 * np.abs(x)) * np.cos(6.0 * x))
        
        # Increased ruggedness through high-frequency oscillations with variable amplitude
        f4 = 0.7 * np.sum(np.sin(25.0 * x) * np.exp(-0.03 * x**2))
        
        # Additional chaotic term with logistic-like behavior and cosine modulation
        f5 = 0.3 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.1 * np.abs(x)) * np.sin(7.0 * x))
        
        # Combine all components with optimized weights
        return f1 + 0.4 * f2 + 0.3 * f3 + 0.2 * f4 + 0.1 * f5