import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal weights for Brownian motion
        self.fractal_weights = np.array([1.0 / (2**i) for i in range(10)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with mixed monomials
        poly_chaos = np.sum(
            np.array([1.2, -1.8, 2.5, -3.1, 3.7, -4.2, 4.8, -5.3, 5.9, -6.4]) * 
            np.power(np.abs(x), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        )
        
        # Fractal Brownian motion component with multiple scales
        fbm = 0.0
        for i in range(min(5, len(self.fractal_weights))):
            scale = 2**i
            fbm += self.fractal_weights[i] * np.sum(
                np.sin(scale * np.pi * x) * np.cos(scale * np.pi * x) * 
                np.sin(scale * 0.5 * np.pi * x) * np.cos(scale * 0.5 * np.pi * x)
            )
        
        # Adaptive coupling with dynamic weights based on variable positions
        adaptive_coupling = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1.0 + np.exp(-0.5 * (x[i] - x[i+1])**2))
            adaptive_coupling += weight * (
                (x[i] - x[i+1])**3 * np.sin(10 * np.pi * x[i]) * 
                np.cos(8 * np.pi * x[i+1]) + 
                (x[i] + x[i+1])**2 * np.cos(6 * np.pi * x[i]) * 
                np.sin(4 * np.pi * x[i+1])
            )
        
        # Multi-scale sinusoidal modulation with varying frequencies
        modulated = np.sum(
            np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
            np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * 
            np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
            np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x) * 
            np.sin(4 * np.pi * x) * np.cos(2 * np.pi * x)
        )
        
        # Hybrid exponential-polynomial term
        exp_poly = np.sum(
            np.exp(-0.5 * x**2) * (1.0 + 0.5 * np.sin(15 * np.pi * x)) * 
            (1.0 + 0.3 * np.cos(12 * np.pi * x)) * 
            (1.0 + 0.2 * np.sin(9 * np.pi * x))
        )
        
        # Global offset and scaling
        return 0.3 * poly_chaos + 0.25 * fbm + 0.2 * adaptive_coupling + 0.15 * modulated + 0.1 * exp_poly + 3.5