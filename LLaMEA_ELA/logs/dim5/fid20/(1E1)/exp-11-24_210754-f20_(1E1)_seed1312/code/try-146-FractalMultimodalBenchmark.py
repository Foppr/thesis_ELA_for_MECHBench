import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal-like structure with recursive chaotic scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased frequency and chaotic modulation
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 1.2)) * (1.0 + 0.5 * np.cos(i * 0.9))
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.3) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Higher-order polynomial corruption with increased fractional powers
        f3 = 0.05 * np.sum((x**6.7 + 1.2 * x**5.9 + 0.9 * x**3.8 + 0.4 * x**3.2) / self.dim)
        
        # Complex saddle point structure with multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Enhanced fractal self-similarity with increased frequency components
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)))
        
        # Stronger cross-term interactions with asymmetric coupling and higher nonlinearity
        f6 = 0.1 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.3 * x[:-1] - x[1:]))
        
        # Increased fractional Brownian motion-like roughness with higher variance
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Additional high-frequency interference terms for increased complexity
        f9 = 0.12 * np.sum(np.sin(80.0 * x) * np.cos(65.0 * x) * np.exp(-0.2 * x**2))
        
        # Combined fitness with adjusted weights
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9