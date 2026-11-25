import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic behavior
        f1 = np.sum(x**2) / self.dim
        
        # Exponential decay modulated by sinusoidal interference
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic modulation with exponential decay and trigonometric interference
            f2 += np.exp(-0.5 * xi**2) * np.sin(10.0 * xi) * np.cos(7.0 * xi)
        
        # Power-law scaling with fractional exponents and multi-scale interactions
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractional power terms with varying exponents
            f3 += (np.abs(xi)**1.7 + 0.5 * np.abs(xi)**2.3 + 0.2 * np.abs(xi)**3.1) / self.dim
        
        # Multi-scale sinusoidal interference with varying frequencies and amplitudes
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 * (1.0 + 0.3 * np.sin(i * 0.7)) * (1.0 + 0.2 * np.cos(i * 0.4))
            f4 += np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Asymmetric saddle point structure with exponential curvature
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric exponential curvature with varying scale
            f5 += (xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(5.0 * xi)
        
        # Cross-dimensional interaction terms with asymmetric coupling
        f6 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            # Asymmetric coupling with power-law interaction
            f6 += (xi**1.3 * xj**1.7 + 0.5 * xi**2.1 * xj**1.9) / self.dim
        
        # Ruggedness from fractional Brownian motion-like roughness
        f7 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractional scaling with roughness modulation
            f7 += np.abs(xi)**1.4 * np.sin(15.0 * xi) * np.cos(8.0 * xi)
        
        # Combined chaotic and multi-modal structure with nonlinearity
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.25 * f4 + 0.15 * f5 + 0.1 * f6 + 0.1 * f7