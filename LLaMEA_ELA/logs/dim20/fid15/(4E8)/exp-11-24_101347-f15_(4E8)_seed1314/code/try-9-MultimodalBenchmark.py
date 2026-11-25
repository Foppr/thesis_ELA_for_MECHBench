import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 2.0) * np.cos(r)
        
        # Trigonometric waves in different directions
        wave1 = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        wave2 = np.sum(np.cos(4.0 * x) * np.sin(1.5 * x))
        
        # Chaotic component using sine of squared coordinates
        chaotic = np.sum(np.sin(x**2) * np.cos(x))
        
        # Combine all components with different weights
        result = 0.4 * radial + 0.3 * wave1 + 0.2 * wave2 + 0.1 * chaotic
        
        return result