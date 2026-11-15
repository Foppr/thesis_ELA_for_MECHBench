import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Chaotic sinusoidal modulation with exponential decay
        f2 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * np.cos(15.0 * x))
        
        # Multi-scale oscillatory component with varying frequencies
        f3 = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.sin(8.0 * x) * np.cos(16.0 * x))
        
        # Cross-dimensional interaction with exponential coupling
        f4 = np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * np.sin(5.0 * (x[:-1] + x[1:])) * np.cos(3.0 * (x[:-1] - x[1:])))
        
        # Fractal-like component with recursive structure
        f5 = np.sum(np.sin(20.0 * x) * np.cos(25.0 * x) * np.sin(30.0 * x) * np.cos(35.0 * x) * np.exp(-0.05 * x**2))
        
        # Gradient-based chaotic component with directional sensitivity
        f6 = np.sum(np.exp(-0.2 * x**2) * np.sin(25.0 * x) * np.cos(30.0 * x) * np.sin(35.0 * x))
        
        # High-frequency oscillation with amplitude modulation
        f7 = np.sum(np.sin(50.0 * x) * np.cos(60.0 * x) * np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * np.sum(x**2)))
        
        # Combined function with dynamic weights and normalization
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.08 * f6 + 0.02 * f7