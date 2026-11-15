import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.5 * np.sum(x**2)
        
        # Chaotic Gaussian peaks with varying widths and positions
        f2 = 0.0
        for i in range(self.dim):
            sigma = 0.5 + 0.5 * np.sin(i * 0.7)
            mu = 2.0 * np.cos(i * 0.3)
            f2 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**2) * (1.0 + 0.3 * np.sin(5.0 * x[i]))
        
        # Trigonometric interaction terms creating complex interference patterns
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f3 += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Non-convex penalty term with multiple local minima
        f4 = 0.3 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Exponentially decaying chaotic component
        f5 = 0.2 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.exp(-0.2 * np.abs(x)))
        
        # Multi-scale sinusoidal modulation
        f6 = 0.15 * np.sum(np.sin(2.0 * x) * np.sin(4.0 * x) * np.sin(8.0 * x) * np.exp(-0.05 * x**2))
        
        # Asymmetric long-range interaction
        f7 = 0.1 * np.sum(np.sin(0.1 * x) * np.exp(-0.01 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7