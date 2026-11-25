import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global attraction
        f1 = np.sum(x**2)
        
        # Chaotic sinusoidal modulation with exponential decay
        f2 = 0.5 * np.sum(np.sin(np.exp(1.5 * np.abs(x))) * np.exp(-0.3 * x**2))
        
        # Additional cosine modulation with frequency scaling
        f3 = 0.3 * np.sum(np.cos(3.0 * np.log(np.abs(x) + 1.0)) * np.exp(-0.1 * x**2))
        
        # Logarithmic barrier terms to create steep gradients near boundaries
        f4 = 0.2 * np.sum(np.log(26.0 - (x**2))) * (np.abs(x) > 2.0)
        
        # Mixed polynomial and trigonometric terms for complexity
        f5 = 0.1 * np.sum((x**3) * np.sin(2.0 * x))
        
        # Fractal-like perturbation using recursive sine composition
        f6 = 0.05 * np.sum(np.sin(np.sin(np.sin(x))))
        
        return f1 + f2 + f3 + f4 + f5 + f6