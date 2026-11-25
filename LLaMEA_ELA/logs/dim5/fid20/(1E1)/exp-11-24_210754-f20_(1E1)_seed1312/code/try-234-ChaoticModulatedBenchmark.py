import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Exponential decay with trigonometric modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic frequency modulation
            freq = 10.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.9))
            f2 += np.exp(-0.5 * xi**2) * np.sin(freq * xi)**2
        
        # Polynomial modulation with fractional powers and varying coefficients
        f3 = 0.05 * np.sum((x**4.7 + 0.9 * x**3.8 + 0.6 * x**2.5 + 0.3 * x**1.9) / self.dim)
        
        # Multi-scale interference with asymmetric coupling
        f4 = 0.1 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Fractal-like recursive modulation with increasing frequency
        f5 = 0.15 * np.sum(np.sin(30.0 * np.sin(5.0 * x)) * np.cos(25.0 * np.cos(4.0 * x)))
        
        # Asymmetric saddle points with exponential curvature
        f6 = 0.2 * np.sum((x**3.2 + 0.5 * x**2.1 - 0.3 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Cross-dimensional interaction with chaotic coupling
        f7 = 0.08 * np.sum(np.sin(0.5 * x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with exponential scaling
        f8 = 0.12 * np.sum(np.abs(x)**1.7 * np.sin(18.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8