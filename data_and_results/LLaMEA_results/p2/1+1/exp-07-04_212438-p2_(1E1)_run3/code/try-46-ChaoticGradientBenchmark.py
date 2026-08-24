import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like component with recursive sine-cosine structure
        f1 = np.sum(np.sin(10.0 * np.sin(5.0 * x)) * np.cos(8.0 * np.cos(7.0 * x)) * np.exp(-0.1 * x**2))
        
        # Dynamic conditioning with variable exponent and coupling
        f2 = np.sum((x**2 + 0.1) * np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Saddle-point clustering with multiple local minima and maxima
        f3 = np.sum(np.sin(12.0 * x) * np.cos(12.0 * x) * np.exp(-0.2 * (x - 1.0)**2) * np.exp(-0.2 * (x + 1.0)**2))
        
        # Chaotic feedback component with time-delayed interactions
        f4 = np.sum(np.sin(25.0 * x[:-1]) * np.cos(25.0 * x[1:]) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * np.sin(3.0 * np.sum(x**2)))
        
        # Multi-scale oscillatory component with varying frequencies and amplitudes
        f5 = np.sum(np.sin(30.0 * x) * np.cos(35.0 * x) * np.sin(40.0 * x) * np.cos(45.0 * x) * np.exp(-0.15 * x**2))
        
        # Gradient-based chaotic modulation with non-linear damping
        f6 = np.sum(np.sin(50.0 * x) * np.cos(55.0 * x) * np.exp(-0.3 * np.abs(x)) * np.sin(2.0 * np.sum(np.sin(x))))
        
        # Cross-dimensional coupling with hyperbolic tangent modulation
        f7 = np.sum(np.tanh(10.0 * x) * np.sin(15.0 * x) * np.cos(20.0 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Fractal dimensionality scaling with recursive structure
        f8 = np.sum(np.sin(60.0 * x) * np.cos(65.0 * x) * np.sin(70.0 * x) * np.cos(75.0 * x) * np.exp(-0.1 * x**3))
        
        # Combined function with weighted normalization and chaotic amplification
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.08 * f6 + 0.07 * f7 + 0.05 * f8