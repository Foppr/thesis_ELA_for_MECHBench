import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        f2 = 0.25 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Add a more complex interaction term to create challenging landscape
        f3 = 0.2 * np.sum(np.sin(3 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Introduce a quartic term for increased non-convexity
        f4 = 0.03 * np.sum(x_norm**4)
        
        # Add a cross-term interaction to make optimization more challenging
        f5 = 0.06 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(6 * np.pi * x_norm[:-1]))
        
        # Introduce a new interaction term with higher frequency components
        f6 = 0.1 * np.sum(np.cos(8 * np.pi * x_norm) * np.sin(9 * np.pi * x_norm))
        
        # Combine all terms with different weights to control difficulty
        return f1 + f2 + f3 + f4 + f5 + f6