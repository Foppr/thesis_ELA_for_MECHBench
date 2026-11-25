import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Logarithmic transformation component with small offset to avoid singularity
        f2 = 0.3 * np.sum(np.log(np.abs(x_norm) + 1e-8))
        
        # Exponential coupling terms between dimensions
        f3 = 0.2 * np.sum(np.exp(-x_norm[:-1] * x_norm[1:]))
        
        # Multi-scale sinusoidal modulations with varying frequencies
        f4 = 0.25 * np.sum(np.sin(5 * np.pi * x_norm) + 0.5 * np.sin(15 * np.pi * x_norm))
        
        # Cross-dimensional polynomial interactions
        f5 = 0.1 * np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * (x_norm[:-1] + x_norm[1:]))
        
        # Hyperbolic tangent modulation for nonlinearity
        f6 = 0.15 * np.sum(np.tanh(3 * x_norm)**2)
        
        # Fifth-order polynomial with alternating signs
        f7 = 0.08 * np.sum((-1)**np.arange(self.dim) * x_norm**5)
        
        # Combine all components
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result