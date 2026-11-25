import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Exponential decay interactions with trigonometric modulation
        f2 = 0.5 * np.sum(np.exp(-5 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm))
        
        # Wave interference pattern with adaptive frequencies
        f3 = 0.3 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                         np.exp(-2 * np.abs(x_norm)))
        
        # Polynomial coupling with exponential decay
        f4 = 0.2 * np.sum(x_norm**5 * np.exp(-3 * np.abs(x_norm)))
        
        # Adaptive trigonometric cross-terms with varying amplitudes
        f5 = 0.25 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                          (1 + 0.5 * np.sin(3 * np.pi * x_norm)))
        
        # Multi-scale exponential interactions
        f6 = 0.15 * np.sum(np.exp(-10 * np.abs(x_norm)) * np.sin(12 * np.pi * x_norm))
        
        # Polynomial cross-terms with adaptive weights
        f7 = 0.1 * np.sum(x_norm**3 * np.cos(5 * np.pi * x_norm) * 
                         np.exp(-4 * np.abs(x_norm)))
        
        # Non-linear frequency modulation with exponential decay
        f8 = 0.12 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                          np.exp(-6 * np.abs(x_norm)) * (x_norm**2 + 0.1))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
        
        return result