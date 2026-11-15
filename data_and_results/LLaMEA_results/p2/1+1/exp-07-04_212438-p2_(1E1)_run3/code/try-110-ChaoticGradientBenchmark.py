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
        chaos_term = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * np.cos(15.0 * x) * np.sin(20.0 * x))
        
        # Gradient-based component with varying step sizes and directional sensitivity
        grad_term = np.sum((x[:-1] - x[1:])**2 * np.exp(-0.5 * (x[:-1] + x[1:])**2))
        
        # Saddle-point attractor with multi-dimensional interaction
        saddle_term = np.sum(np.sin(5.0 * x) * np.cos(5.0 * x) * np.exp(-0.3 * x**2) * np.sin(2.0 * np.sum(x**2)))
        
        # Exponentially decaying correlation structure
        decay_factor = np.exp(-0.2 * np.arange(self.dim))
        corr_term = np.sum(decay_factor * np.sin(8.0 * x) * np.cos(12.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Fractional power interaction with asymmetric weighting
        frac_term = np.sum(np.abs(x)**1.7 * np.sin(7.0 * x) * np.cos(9.0 * x) * np.exp(-0.4 * x**2))
        
        # Multi-scale oscillatory component with varying frequencies and amplitudes
        scale_term = np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * np.exp(-0.1 * np.abs(x)) * np.sin(3.0 * np.sum(x)))
        
        # Combined function with dynamic weights and normalization
        return 0.4 * chaos_term + 0.3 * grad_term + 0.2 * saddle_term + 0.15 * corr_term + 0.1 * frac_term + 0.05 * scale_term