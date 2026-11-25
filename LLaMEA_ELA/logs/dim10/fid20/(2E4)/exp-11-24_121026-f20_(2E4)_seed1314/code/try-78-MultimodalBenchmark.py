import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency trigonometric terms creating multiple local minima
        f2 = np.sum(np.sin(20 * x_norm)**4 + np.cos(15 * x_norm)**4)
        
        # Chaotic logistic-like component with varying parameters
        f3 = np.sum(np.sin(np.pi * x_norm * np.sin(10 * x_norm))**6)
        
        # Polynomial with mixed degrees for additional complexity
        f4 = np.sum(x_norm**5 + 0.5 * x_norm**3 - 0.3 * x_norm)
        
        # Adaptive exponential barrier near boundaries
        f5 = np.sum(np.exp(-2 * x_norm**2) - 1.0 + 0.1 * np.abs(x_norm))
        
        # Fractional power terms for non-smooth behavior
        f6 = np.sum(np.abs(x_norm)**1.3)
        
        # Multi-scale sinusoidal modulation
        f7 = np.sum(np.sin(5 * x_norm * np.cos(8 * x_norm))**3)
        
        # Modified chaotic map with frequency control
        f8 = 0.5 * np.sum(np.sin(3 * np.pi * x_norm * np.sin(12 * x_norm**2))**5)
        
        # Logarithmic barrier near boundaries
        f9 = 0.2 * np.sum(np.log(1 + 0.5 * x_norm**2))
        
        # Fourth-order polynomial with random-like coefficients
        f10 = 0.1 * np.sum((x_norm**4 - 0.8 * x_norm**3 + 0.6 * x_norm**2 - 0.2 * x_norm)**2)
        
        # Combined chaotic and trigonometric term
        f11 = 0.3 * np.sum(np.sin(7 * x_norm * np.sin(5 * x_norm))**4)
        
        # Adaptive scaling factor for different dimensions
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 
                              0.08 * f6 + 0.12 * f7 + 0.15 * f8 + 0.05 * f9 + 
                              0.06 * f10 + 0.1 * f11)