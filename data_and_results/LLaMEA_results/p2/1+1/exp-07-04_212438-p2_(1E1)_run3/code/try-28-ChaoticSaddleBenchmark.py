import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like component with recursive cosine structure
        f1 = np.sum(np.cos(13.0 * x) * np.cos(17.0 * x) * np.cos(19.0 * x) * np.cos(23.0 * x))
        
        # Saddle-point component with alternating hyperbolic tangents
        f2 = np.sum(np.tanh(2.0 * x) * np.tanh(3.0 * x[:-1]) * np.tanh(3.0 * x[1:]) * np.tanh(4.0 * x[:-1] + 4.0 * x[1:]))
        
        # Dynamic gradient modulation with time-varying frequency
        f3 = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * np.abs(x)) * np.sin(0.5 * np.sum(x**2)))
        
        # Embedded chaotic map component with logistic-like dynamics
        f4 = np.sum(np.sin(11.0 * x) * np.cos(13.0 * x) * np.exp(-0.05 * x**2) * np.sin(2.0 * np.sum(np.sin(x))))
        
        # Multi-scale oscillatory component with variable amplitude and frequency
        f5 = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.sin(8.0 * x) * np.cos(16.0 * x) * np.exp(-0.02 * np.abs(x)))
        
        # Non-smooth and piecewise component with sharp transitions
        f6 = np.sum(np.abs(x) * np.sin(10.0 * x) * np.cos(15.0 * x) * np.exp(-0.03 * x**2))
        
        # Coupled oscillator with phase locking and frequency modulation
        f7 = np.sum(np.sin(3.0 * x[:-1]) * np.cos(3.0 * x[1:]) * np.sin(5.0 * (x[:-1] - x[1:])) * np.cos(7.0 * (x[:-1] + x[1:])))
        
        # Fractal dimensionality modulation with recursive scaling
        f8 = np.sum(np.sin(25.0 * x) * np.cos(27.0 * x) * np.sin(29.0 * x) * np.cos(31.0 * x) * np.exp(-0.01 * np.abs(x)**1.5))
        
        # Combined function with dynamic weighting and chaotic amplification
        return 0.15 * f1 + 0.14 * f2 + 0.13 * f3 + 0.12 * f4 + 0.11 * f5 + 0.10 * f6 + 0.10 * f7 + 0.05 * f8