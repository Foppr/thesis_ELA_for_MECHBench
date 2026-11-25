import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = 0.5 * np.sum(np.sin(15 * np.pi * x_norm) + 0.5 * np.sin(23 * np.pi * x_norm))
        
        # Octic polynomial term for deep valleys
        f3 = 0.05 * np.sum(x_norm**8)
        
        # Sextic polynomial term for added complexity
        f4 = 0.03 * np.sum(x_norm**6)
        
        # Quintic cross-term interactions
        f5 = 0.02 * np.sum(x_norm[:-1]**5 * x_norm[1:])
        
        # Septic term with mixed dimensions
        f6 = 0.01 * np.sum(x_norm[:-2]**7 * x_norm[1:-1] * x_norm[2:])
        
        # Additional sinusoidal with exponential decay factor
        f7 = 0.3 * np.sum(np.sin(7 * np.pi * x_norm) * np.exp(-x_norm**2))
        
        # Combine all components with carefully tuned weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result