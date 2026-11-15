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
        
        # Adaptive conditioning with dimension-dependent scaling
        condition_factors = np.arange(1, self.dim + 1) * 0.5 + 1.0
        f2 = np.sum((x**2) * condition_factors * np.sin(5.0 * x) * np.cos(7.0 * x))
        
        # Multi-scale oscillatory interaction with dynamic coupling
        f3 = np.sum(np.sin(15.0 * x[:-1] * x[1:]) * np.cos(13.0 * x[:-1] + 11.0 * x[1:]) * np.exp(-0.3 * np.abs(x[:-1] - x[1:])))
        
        # Fractal-like recursive interaction with feedback loops
        f4 = np.sum(np.sin(20.0 * np.sin(x)) * np.cos(25.0 * np.cos(x)) * np.exp(-0.2 * x**2))
        
        # Non-separable high-order polynomial with chaotic perturbations
        f5 = np.sum((x**3 + 0.5 * x**2 + 0.3 * x + 0.1) * np.sin(8.0 * x) * np.cos(9.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Dynamic coupling with time-delayed feedback
        f6 = np.sum(np.sin(18.0 * x[:-1]) * np.cos(16.0 * x[1:]) * np.exp(-0.4 * np.abs(x[:-1] - x[1:])) * np.sin(3.0 * np.sum(x)))
        
        # Mixed conditioning and non-linearity with exponential modulation
        f7 = np.sum(np.exp(0.5 * x) * np.sin(14.0 * x) * np.cos(17.0 * x) * np.exp(-0.3 * x**2))
        
        # High-frequency chaotic component with multi-dimensional feedback
        f8 = np.sum(np.sin(40.0 * x) * np.cos(45.0 * x) * np.sin(50.0 * x) * np.cos(55.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all components with adaptive weights
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.10 * f6 + 0.08 * f7 + 0.07 * f8