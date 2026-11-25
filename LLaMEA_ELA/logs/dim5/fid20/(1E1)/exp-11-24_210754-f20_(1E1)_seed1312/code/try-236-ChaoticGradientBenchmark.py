import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic sine-modulated polynomial with dynamic scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            f2 += (scale * np.sin(20.0 * xi) + 0.3 * np.cos(15.0 * xi**2))**4
        
        # Asymmetric saddle point with exponential decay and fractional powers
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f3 += (xi**3.7 + 0.5 * xi**2.3 - 0.8 * xi) * np.exp(-0.2 * np.abs(xi))
        
        # Multi-scale sinusoidal interference with varying frequency and amplitude
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq1 = 10.0 + 5.0 * np.sin(i * 0.5)
            freq2 = 7.0 + 3.0 * np.cos(i * 0.8)
            f4 += np.sin(freq1 * xi) * np.cos(freq2 * xi**1.5)
        
        # Cross-dimensional interaction with dynamic coupling weights
        f5 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            weight = 0.5 + 0.3 * np.sin(i * 0.6)
            f5 += weight * (np.sin(xi + xj) + 0.2 * np.cos(xi - xj))**2
        
        # Fractional Brownian motion-inspired roughness with non-uniform scaling
        f6 = 0.0
        for i in range(self.dim):
            xi = x[i]
            alpha = 1.3 + 0.4 * np.sin(i * 0.9)
            f6 += np.abs(xi)**alpha * np.sin(25.0 * xi)
        
        # Asymmetric cubic polynomial with exponential modulation
        f7 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f7 += (xi**3.1 + 0.4 * xi**2.6 - 0.6 * xi) * np.exp(-0.15 * xi**2)
        
        # Combine all components with adjusted weights
        return f1 + 0.8 * f2 + 0.5 * f3 + 0.6 * f4 + 0.4 * f5 + 0.7 * f6 + 0.9 * f7