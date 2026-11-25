import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(10.0 * x) * np.exp(-0.1 * x**2))
        f3 = 0.25 * np.sum(np.cos(15.0 * x) * np.exp(-0.05 * x**2))
        f4 = 0.2 * np.sum(np.sin(7.0 * x + 1.0) * np.exp(-0.3 * x**2))
        
        # Add a complex fractal-like modulation using multiple cosine terms
        f5 = 0.15 * np.sum(np.cos(20.0 * x) * np.cos(8.0 * x) * np.exp(-0.1 * x**2))
        
        # Add a cubic term with adaptive scaling based on position
        f6 = 0.01 * np.sum(x**3 * (1.0 + 0.5 * np.sin(x)))
        
        # Add a quartic term with exponential decay
        f7 = 0.005 * np.sum(x**4 * np.exp(-0.02 * np.abs(x)))
        
        # Add a fifth-order polynomial term for increased complexity
        f8 = 0.001 * np.sum(x**5)
        
        # Add a chaotic modulation using sine of exponential function
        f9 = 0.1 * np.sum(np.sin(np.exp(x)) * np.cos(x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9