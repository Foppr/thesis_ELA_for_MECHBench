import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension
        self.global_min = np.array([(-1)**i * 2.5 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum((x - self.global_min)**2)
        
        # Sinusoidal modulations with varying frequencies
        f2 = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Polynomial interaction terms
        f3 = np.sum(x**4 - 10 * x**2)
        
        # Exponential penalty for large values
        f4 = np.sum(np.exp(0.2 * np.abs(x)) - 1)
        
        # Chaotic component using sine of sine
        f5 = np.sum(np.sin(np.sin(x)))
        
        # Combine all components with varying weights
        return 0.2 * f1 + 0.3 * f2 + 0.1 * f3 + 0.2 * f4 + 0.2 * f5