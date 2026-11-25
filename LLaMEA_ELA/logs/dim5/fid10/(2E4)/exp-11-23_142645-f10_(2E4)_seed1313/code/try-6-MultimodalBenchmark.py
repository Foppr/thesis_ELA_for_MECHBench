import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 2.0)
        
        # Trigonometric oscillations in multiple directions
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(3.0 * x[i]) * np.cos(2.0 * x[(i + 1) % self.dim])
        
        # Add a quartic penalty term to increase curvature near boundaries
        penalty = 0.01 * np.sum(x**4)
        
        # Combine components with varying weights
        return radial + 0.5 * oscillation + penalty