import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier terms to create sharp, narrow valleys
        f1 = np.sum(np.log(1.0 + 0.1 * x**2) * np.sin(10.0 * x))
        
        # Trigonometric coupling with adaptive frequency modulation
        f2 = 0.5 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Nested periodic components with varying amplitudes and scales
        f3 = 0.3 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * np.sin(9.0 * x))
        
        # Dynamic conditioning based on distance from origin
        condition = 1.0 + 0.5 * np.sum(x**2)
        f4 = 0.2 * np.sum((x**2) * np.sin(5.0 * x) / condition)
        
        # Multi-scale interaction terms with exponential decay
        f5 = 0.15 * np.sum(np.exp(-0.2 * np.abs(x)) * np.cos(8.0 * x) * np.sin(4.0 * x))
        
        # Coupled sine-cosine waves with polynomial modulation
        f6 = 0.25 * np.sum(np.sin(6.0 * x) * np.cos(11.0 * x) * x**3)
        
        # Adaptive scaling with Gaussian-like modulation
        f7 = 0.1 * np.sum(np.exp(-0.1 * np.sum(x**2)) * np.sin(13.0 * x) * np.cos(7.0 * x))
        
        # Additional non-separable interaction term
        f8 = 0.12 * np.sum(np.sin(2.0 * x) * np.cos(5.0 * x) * np.exp(-0.3 * np.sum(x**2)) * x**4)
        
        # Combined landscape with enhanced multimodality and complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8