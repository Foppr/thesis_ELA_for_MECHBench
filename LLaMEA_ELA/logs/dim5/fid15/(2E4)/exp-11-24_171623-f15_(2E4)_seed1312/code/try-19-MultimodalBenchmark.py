import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with varying weights per dimension
        f1 = np.sum((x_norm ** 2) * np.linspace(0.5, 2.0, self.dim))
        
        # Nested sinusoidal terms with frequency modulation based on dimension index
        f2 = np.sum(np.sin(3 * np.pi * x_norm * (1 + 0.5 * np.arange(self.dim))) ** 2)
        
        # Product of cosines with varying frequencies and phase shifts
        f3 = np.prod(np.cos(1.5 * np.pi * x_norm + 0.3 * np.arange(self.dim)))
        
        # Cubic polynomial with mixed signs for additional complexity
        f4 = np.sum(x_norm ** 3 * np.random.uniform(-1, 1, self.dim))
        
        # Global sinusoidal modulation to create large-scale structure
        global_mod = np.sin(0.5 * np.pi * np.sum(x_norm ** 2))
        
        # Combine all terms with adaptive weights and global modulation
        result = 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + 0.5 * global_mod
        
        return result