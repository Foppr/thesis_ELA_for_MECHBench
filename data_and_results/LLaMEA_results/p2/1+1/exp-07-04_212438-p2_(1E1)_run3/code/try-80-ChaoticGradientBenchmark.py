import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay component with sinusoidal modulation
        f1 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * np.cos(12.0 * x))
        
        # Multi-dimensional coupling with exponentially decaying weights
        weights = np.exp(-0.5 * np.arange(self.dim))
        f2 = np.sum(weights * (x[:-1] - x[1:])**2 * np.sin(8.0 * (x[:-1] + x[1:])))
        
        # Fractional power chaotic component with dynamic scaling
        f3 = np.sum(np.abs(x)**1.7 * np.sin(15.0 * x) * np.cos(18.0 * x) * np.exp(-0.3 * x**2))
        
        # Cross-dimensional interaction with time-delayed feedback
        f4 = np.sum(np.sin(20.0 * x[:-1]) * np.cos(22.0 * x[1:]) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * np.sin(5.0 * np.sum(x)))
        
        # Multi-scale oscillatory component with varying frequencies and amplitudes
        f5 = np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * np.sin(35.0 * x) * np.cos(40.0 * x) * np.exp(-0.4 * x**2))
        
        # Non-separable component with recursive-like structure
        f6 = np.sum(np.sin(12.0 * x[:-1]) * np.cos(14.0 * x[1:]) * np.sin(16.0 * (x[:-1] + x[1:])) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # Fractal-like component with nested sinusoidal modulations
        f7 = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.sin(9.0 * x) * np.cos(11.0 * x) * np.exp(-0.6 * np.abs(x)**1.5))
        
        # Asymmetric gradient component with varying decay rates
        f8 = np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(20.0 * x) * np.cos(25.0 * x) * (x**2 + 1.0)**(-0.5))
        
        # Combined function with dynamic weighting and normalization
        return 0.42 * f1 + 0.38 * f2 + 0.35 * f3 + 0.33 * f4 + 0.31 * f5 + 0.28 * f6 + 0.25 * f7 + 0.22 * f8