import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize a pseudo-random seed for time-varying behavior
        np.random.seed(42)
        self.shift_pattern = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x**4 + 0.5 * x**3 + 0.1 * x**2)
        
        # Trigonometric terms with varying frequencies and phases
        f2 = np.sum(np.sin(2.0 * x + np.pi/4) * np.cos(3.0 * x + np.pi/6))
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        f3 = np.sum(np.exp(-0.1 * r) * np.sin(5.0 * r))
        
        # Cross-terms creating complex interactions
        f4 = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]))
        
        # Time-varying global minimum shift
        shift = self.shift_pattern * np.sin(np.sum(x) * 0.1)
        f5 = np.sum((x - shift)**2)
        
        # Combine all terms with different weights
        return 0.2 * f1 + 0.3 * f2 + 0.25 * f3 + 0.15 * f4 + 0.1 * f5