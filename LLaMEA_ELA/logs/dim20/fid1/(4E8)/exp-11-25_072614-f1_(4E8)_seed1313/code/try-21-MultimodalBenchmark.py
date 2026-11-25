import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 5.0) * (1.0 + 0.5 * np.sin(r))
        
        # Trigonometric interference terms
        trig_interference = np.sum(np.cos(3.0 * x) * np.sin(7.0 * x))
        
        # Add a chaotic component using sine of squared coordinates
        chaotic = np.sum(np.sin(x**2) * np.cos(x))
        
        # Combine all components with different weights
        return radial + 0.3 * trig_interference + 0.1 * chaotic + 0.01 * r**3