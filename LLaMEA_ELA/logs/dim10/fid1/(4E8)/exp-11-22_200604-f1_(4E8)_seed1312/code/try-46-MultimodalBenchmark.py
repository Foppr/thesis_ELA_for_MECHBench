import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base function
        f1 = np.sum(x_norm**2)
        
        # Exponentially decaying harmonic terms with varying frequencies
        f2 = 0.5 * np.sum(np.exp(-np.abs(x_norm)) * np.sin(5 * np.pi * x_norm))
        
        # Asymmetric cubic cross-terms to create skewed valleys
        f3 = 0.1 * np.sum((x_norm[:-1] + x_norm[1:]) ** 3)
        
        # Higher-order polynomial with alternating signs for complex curvature
        f4 = 0.05 * np.sum(x_norm**5 - 2 * x_norm**3 + x_norm)
        
        # Multi-scale sinusoidal components to introduce multiple scales of optima
        f5 = 0.2 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Asymmetric basin structure using modified exponential decay
        f6 = 0.15 * np.sum(np.exp(-0.5 * (x_norm - 0.3)**2) * np.sin(8 * np.pi * x_norm))
        
        # Cross-dimensional interaction with weighted coupling
        f7 = 0.08 * np.sum(x_norm[:-2] * x_norm[1:-1] * x_norm[2:] * (x_norm[:-2] + x_norm[1:-1] + x_norm[2:]))
        
        # Final combination with carefully balanced weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result