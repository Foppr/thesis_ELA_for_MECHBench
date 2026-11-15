import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x**4 - 2*x**2)
        
        # Trigonometric terms with multiple frequencies
        f2 = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Logarithmic terms to create sharp gradients
        f3 = np.sum(np.log(1.0 + 0.1 * x**2))
        
        # Chaotic component using sine of exponential
        f4 = np.sum(np.sin(np.exp(x)))
        
        # Combine all terms with different weights
        return 0.2 * f1 + 0.3 * f2 + 0.25 * f3 + 0.25 * f4