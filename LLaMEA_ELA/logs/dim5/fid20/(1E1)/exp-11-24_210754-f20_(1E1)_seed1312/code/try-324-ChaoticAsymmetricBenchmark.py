import numpy as np

class ChaoticAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with exponential scaling
        f1 = np.sum(np.exp(0.1 * x**2)) / self.dim
        
        # Trigonometric interference with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 + 15.0 * np.sin(i * 0.7)
            amp = 1.0 + 0.5 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Asymmetric polynomial potentials with fractional exponents
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Different behavior for positive and negative values
            if xi >= 0:
                f3 += 0.5 * xi**3.2 + 0.3 * xi**1.8
            else:
                f3 += 0.7 * xi**4.1 + 0.2 * xi**2.3
        
        # Exponential decay with sinusoidal modulation for multi-scale structure
        f4 = 0.15 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Cross-dimensional coupling with asymmetric interaction weights
        f5 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            # Asymmetric coupling: different influence based on variable order
            f5 += (0.8 * np.sin(xi + 0.6 * xj) + 0.4 * np.cos(1.2 * xi - xj))**2
        
        # Fractal-like recursive structure with nested exponential terms
        f6 = 0.1 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(50.0 * np.sin(5.0 * x)))
        
        # Add noise-like perturbations using fractional Brownian motion-inspired terms
        f7 = 0.08 * np.sum(np.abs(x)**1.7 * np.cos(25.0 * x))
        
        # Combine all components with dimensionality-dependent scaling
        return f1 + f2 + f3 + f4 + f5 + f6 + f7