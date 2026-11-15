import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Trigonometric component with varying frequencies and phases
        trig = 0
        for i in range(self.dim):
            trig += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function component with multiple centers
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rbf += np.exp(-0.5 * (x[i] - center)**2) * np.sin(5 * (x[i] - center))
        
        # Cross-term interactions with varying coupling strengths
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            cross += (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j])**2)
        
        # Scale and combine components
        return 0.3 * poly + 0.4 * trig + 0.2 * rbf + 0.1 * cross