import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal oscillations with logarithmic frequency modulation
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * np.log(np.abs(x) + 1e-8) * x))
        
        # Polynomial corruption with varying degrees and adaptive coefficients
        f3 = 0.02 * np.sum(0.8 * x**7 + 0.5 * x**6 + 0.4 * x**5 + 0.2 * x**4 + 0.1 * x**3)
        
        # Add saddle point structure with stronger interaction and adaptive scaling
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.9 * x) * np.exp(-0.15 * np.abs(x)) * (1 + 0.1 * np.sin(x)))
        
        # Introduce additional chaotic component with adaptive frequency
        f5 = 0.07 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tan(0.5 * x))
        
        # Add a conditioning term to increase ill-conditioning
        f6 = 0.03 * np.sum((x**2 + 0.1 * np.sin(10 * x)) * np.exp(-0.05 * np.abs(x)))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6