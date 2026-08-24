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
        f2 = np.sum(np.exp(-0.35 * x**2) * np.sin(4.0 * x))
        
        # Chaotic component using sine-cosine product with modified decay
        f3 = np.sum(np.sin(x) * np.cos(3.0 * x) * np.exp(-0.25 * np.abs(x)) * np.cos(6.0 * x))
        
        # Increased ruggedness through high-frequency oscillations with variable amplitude
        f4 = 0.7 * np.sum(np.sin(25.0 * x) * np.exp(-0.03 * x**2))
        
        # Additional chaotic term with logistic-like behavior and cosine modulation
        f5 = 0.3 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.1 * np.abs(x)) * np.sin(7.0 * x))
        
        # New component: modified cosine modulation with altered decay and added interaction
        f6 = 0.2 * np.sum(np.cos(5.0 * x) * np.exp(-0.15 * x**2) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Additional interaction term between dimensions to increase complexity
        f7 = 0.1 * np.sum(np.sin(x[:-1] - x[1:]) * np.cos(3.0 * x[:-1] + x[1:]))
        
        # Combine all components with optimized weights
        return f1 + 0.4 * f2 + 0.3 * f3 + 0.2 * f4 + 0.1 * f5 + 0.15 * f6 + 0.05 * f7