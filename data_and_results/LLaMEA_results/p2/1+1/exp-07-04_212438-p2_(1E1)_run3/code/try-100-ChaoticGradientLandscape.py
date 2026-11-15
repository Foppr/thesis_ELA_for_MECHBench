import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Chaotic sine component with exponentially decaying frequency
        f2 = np.sum(np.sin(20.0 * np.exp(-0.1 * np.abs(x))) * np.cos(15.0 * np.exp(-0.05 * np.abs(x))))
        
        # Multi-scale fractal-like interaction with varying exponents
        f3 = np.sum(np.sin(10.0 * x) * np.cos(12.0 * x) * np.exp(-0.5 * np.abs(x)) * 
                   np.sin(5.0 * np.sum(x**3)) * np.cos(3.0 * np.sum(x**2)))
        
        # Exponentially decaying correlation structure
        decay = np.exp(-0.2 * np.arange(self.dim))
        correlated_terms = np.array([np.sum(x[i:] * decay[i:]) for i in range(self.dim)])
        f4 = np.sum(correlated_terms**2)
        
        # Gradient-based chaotic modulation with time-delayed feedback
        delayed_x = np.roll(x, 1)
        f5 = np.sum(np.sin(25.0 * (x + 0.3 * delayed_x)) * np.cos(22.0 * (x - 0.2 * delayed_x)) * 
                   np.exp(-0.3 * x**2) * np.sin(4.0 * np.sum(x**2)))
        
        # Multi-scale oscillatory component with varying amplitudes
        f6 = np.sum(np.sin(30.0 * x) * np.cos(28.0 * x) * 
                   np.exp(-0.1 * np.abs(x)) * np.sin(8.0 * np.sum(x**4)) * 
                   np.cos(6.0 * np.sum(x**3)))
        
        # Combined function with dynamic weights and normalization
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.10 * f6