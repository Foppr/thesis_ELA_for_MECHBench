import numpy as np

class ExponentialTrigonometricHybrid:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component with dynamic scaling
        f1 = np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        f2 = np.sum(np.exp(-0.1 * np.abs(x)) * np.cos(2.0 * np.pi * x))
        
        # Multi-modal trigonometric component with varying frequencies
        f3 = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.sin(9.0 * x))
        
        # Cross-dimensional interaction with exponential coupling
        f4 = np.sum(np.exp(-0.5 * np.sum((x[:-1] - x[1:])**2)) * np.sin(3.0 * (x[:-1] + x[1:])))
        
        # Fractional power and logarithmic modulation
        f5 = np.sum(np.abs(x)**1.5 * np.log(1.0 + np.abs(x)))
        
        # Chaotic-like component with recursive feedback
        f6 = np.sum(np.sin(10.0 * x) * np.cos(12.0 * x) * np.exp(-0.3 * x**2) * np.sin(4.0 * np.sum(x**2)))
        
        # Dynamic scaling based on dimension
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with weighted sum
        return scale_factor * (0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.08 * f5 + 0.02 * f6)