import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # Exponentially increasing sinusoidal terms for high multimodality
        f2 = np.sum(np.exp(2 * np.abs(x_normalized)) * np.sin(10 * np.pi * x_normalized))
        
        # Cubic interaction terms to create complex valleys and ridges
        f3 = np.sum(x_normalized**3)
        
        # Product of shifted sinusoids for additional local optima
        f4 = np.prod(np.sin(3 * np.pi * x_normalized + 0.5))
        
        # Combine all terms with varying weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4