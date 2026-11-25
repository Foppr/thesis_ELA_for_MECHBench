import numpy as np

class ChaoticCoupledBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Exponential decay with trigonometric coupling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Coupling with neighbor using sine and cosine
            coupling = np.sin(xi) * np.cos(0.5 * xi)
            # Exponential decay term
            decay = np.exp(-0.1 * np.abs(xi))
            f2 += coupling * decay
        
        # Power-law interaction terms with varying exponents
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Power-law with fractional exponent
            power_term = np.abs(xi)**(1.7 + 0.3 * np.sin(i))
            f3 += power_term
        
        # Multi-scale trigonometric interference
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency components
            freq1 = 5.0 * (i + 1)
            freq2 = 3.0 * (i + 1)**1.5
            interference = np.sin(freq1 * xi) * np.cos(freq2 * xi)
            f4 += interference**2
        
        # Asymmetric saddle points with exponential scaling
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric exponential term
            asym_term = (np.exp(0.3 * xi) - np.exp(-0.3 * xi))**2
            f5 += asym_term
        
        # Cross-dimensional coupling with polynomial interaction
        f6 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            # Polynomial coupling with mixed powers
            coupling = (xi**2 + 0.5 * xj**1.5) * np.sin(xi * xj)
            f6 += coupling
        
        # Fractal-like self-similarity through recursive scaling
        f7 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Recursive fractal scaling
            scale = 1.0 + 0.2 * np.sin(xi)
            fractal = np.sin(scale * xi) * np.cos(scale**2 * xi)
            f7 += fractal**2
        
        # Combine all components with adjusted weights
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.25 * f4 + 0.15 * f5 + 0.1 * f6 + 0.1 * f7