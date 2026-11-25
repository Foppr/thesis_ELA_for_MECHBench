import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term with conditioning
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal modulations creating many local minima
        f2 = 0.2 * np.sum(np.sin(15 * np.pi * x_normalized))
        
        # Multi-scale cosine interaction terms
        f3 = np.prod(np.cos(2.0 * x_normalized)) + 0.5 * np.prod(np.cos(4.0 * x_normalized))
        
        # Fourth-order polynomial interactions for sharper curvature
        f4 = 0.1 * np.sum(x_normalized**4)
        
        # Cross-dimensional interaction with exponential decay
        f5 = 0.05 * np.sum(np.exp(-0.5 * np.sum((x_normalized[:, None] - x_normalized[None, :])**2, axis=0)))
        
        # Fifth-order polynomial term for increased complexity
        f6 = 0.03 * np.sum(x_normalized**5)
        
        # Combined function with enhanced multimodality and conditioning
        return f1 + f2 + 0.7 * f3 + f4 + f5 + f6 + 0.05 * np.sum(x_normalized**6)