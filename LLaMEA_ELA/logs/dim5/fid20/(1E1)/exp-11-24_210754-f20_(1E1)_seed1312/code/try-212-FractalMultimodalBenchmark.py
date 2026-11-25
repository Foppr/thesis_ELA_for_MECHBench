import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal structure with recursive chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency scaling with logistic map influence
            freq = 45.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Multi-scale chaotic modulation with fractional powers
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.3) * np.exp(-0.3 * np.abs(xi)**1.7)
            f2 += mod**2
        
        # Polynomial corruption with higher-order terms and variable exponents
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.4 + 0.7 * x**3.8 + 0.4 * x**2.5 + 0.2 * x**1.9) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity with higher frequency components and nested scaling
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and increased complexity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and complexity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and fractional scaling
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**1.8) * np.exp(-0.15 * np.abs(x)))
        
        # Additional chaotic component with nested trigonometric functions
        f9 = 0.12 * np.sum(np.sin(30.0 * np.cos(15.0 * x)) * np.cos(20.0 * np.sin(8.0 * x)) * np.exp(-0.25 * np.abs(x)**1.4))
        
        # Combined fitness with adjusted weights for better discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9