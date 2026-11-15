import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term for global convergence
        f1 = np.sum(x**4)
        
        # Trigonometric components with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(2.0 * x) * np.cos(5.0 * x) * np.sin(8.0 * x))
        
        # Exponential modulation with radial dependence
        f3 = 0.2 * np.sum(np.exp(-0.5 * x**2) * np.sin(3.0 * x))
        
        # Cross-dimensional interaction terms
        f4 = 0.1 * np.sum(np.sin(x) * np.cos(x[None, :] * x[:, None]) * np.exp(-0.1 * np.sum(x**2)))
        
        # Adaptive penalty based on distance from origin with exponential decay
        f5 = 0.15 * np.sum(np.exp(-0.2 * np.sum(x**2)) * x**3)
        
        # Additional multimodal term with Gaussian-like peaks
        f6 = 0.08 * np.sum(np.exp(-0.5 * (x - 1.0)**2) + np.exp(-0.5 * (x + 1.0)**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6