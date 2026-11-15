import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component with exponential decay and sinusoidal modulation
        f1 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * np.cos(15.0 * x) * np.sin(20.0 * x))
        
        # Multi-scale harmonic interactions with varying frequencies and amplitudes
        f2 = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.sin(8.0 * x) * np.cos(16.0 * x) * 
                   np.exp(-0.05 * x**2) * np.sin(3.0 * np.sum(x**2)))
        
        # Exponentially decaying correlation structure with cross-dimensional interactions
        f3 = np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * np.sin(12.0 * (x[:-1] + x[1:])) * 
                   np.cos(14.0 * (x[:-1] - x[1:])) * np.exp(-0.1 * np.abs(x[:-1] + x[1:])))
        
        # Fractional power chaotic component with dynamic scaling
        f4 = np.sum(np.abs(x)**1.7 * np.sin(25.0 * x) * np.cos(30.0 * x) * np.exp(-0.3 * x**2))
        
        # Complex interaction term with recursive-like structure and varying coupling
        f5 = np.sum(np.sin(5.0 * x[:-1]) * np.cos(7.0 * x[1:]) * np.sin(9.0 * x[:-1]) * 
                   np.cos(11.0 * x[1:]) * np.exp(-0.15 * np.abs(x[:-1] - x[1:])) * 
                   np.sin(2.5 * np.sum(x**3)))
        
        # High-frequency oscillatory component with amplitude modulation and phase shifts
        f6 = np.sum(np.sin(40.0 * x) * np.cos(45.0 * x) * np.sin(50.0 * x) * 
                   np.cos(55.0 * x) * np.exp(-0.25 * x**2) * np.sin(1.5 * np.sum(x**4)))
        
        # Combined function with weighted nonlinear interactions and chaotic amplification
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.10 * f6