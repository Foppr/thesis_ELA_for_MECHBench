import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic gradient modulation using logistic map-inspired scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaos parameter based on dimension index
            r = 3.8 + 0.2 * np.sin(i * 0.7)
            # Logistic map-like chaotic behavior
            chaos = r * xi * (1 - xi)
            # Sinusoidal modulation with chaotic scaling
            mod = np.sin(20.0 * xi) * np.cos(15.0 * xi**2) * np.exp(-0.1 * np.abs(xi))
            f2 += mod**2
        
        # Multi-scale sinusoidal interference with varying amplitudes
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency components
            freqs = [5.0, 10.0, 15.0, 20.0]
            for freq in freqs:
                f3 += np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.2 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Fractional power corruption with varying exponents
        f5 = 0.1 * np.sum((np.abs(x)**3.7 + 0.6 * np.abs(x)**2.9 + 0.3 * np.abs(x)**1.8) / self.dim)
        
        # Asymmetric coupling between variables
        f6 = 0.05 * np.sum(np.sin(0.8 * x[:-1] + 1.2 * x[1:]) * np.cos(1.0 * x[:-1] - 0.7 * x[1:]))
        
        # Embedded chaotic gradient with varying curvature
        f7 = 0.15 * np.sum(np.sin(30.0 * np.sin(5.0 * x)) * np.cos(25.0 * np.cos(4.0 * x)))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7