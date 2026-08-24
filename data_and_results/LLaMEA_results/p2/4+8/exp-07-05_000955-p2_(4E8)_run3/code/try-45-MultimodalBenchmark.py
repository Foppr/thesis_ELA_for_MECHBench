import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic multimodal component with sine-cosine interactions
        f2 = 0.2 * np.sum(np.sin(8.0 * x) * np.cos(3.0 * x) * np.sin(2.0 * x))
        
        # Radial basis function with adaptive scaling
        f3 = 0.15 * np.sum(np.exp(-0.5 * np.sum((x[:, np.newaxis] - np.linspace(-5, 5, 10))**2, axis=0)) / 10.0)
        
        # High-order polynomial with exponential modulation
        f4 = 0.1 * np.sum((x**5) * np.exp(-0.1 * np.abs(x)))
        
        # Additional chaotic exponential penalty terms
        f5 = 0.05 * np.sum(np.exp(2.0 * np.abs(x)) - 1.0)
        
        # Adaptive cubic and quartic terms
        f6 = 0.08 * np.sum(x**4 * np.cos(5.0 * x))
        
        # Global conditioning penalty
        f7 = 0.03 * np.sum(np.abs(x)**1.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7