import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal-like behavior with modified interaction terms
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased frequency and chaotic scaling for better discrimination
            freq = 40.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Modified logistic-like modulation with higher nonlinearity
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.8) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Polynomial corruption with increased complexity and fractional powers
        f3 = 0.04 * np.sum((x**5.5 + 0.9 * x**4.7 + 0.6 * x**3.2 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with enhanced interference patterns
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Fractal self-similarity with higher frequency components and sharper transitions
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and stronger nonlinearity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and sharper features
        f7 = 0.15 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.3 - 0.5 * x**2) * np.exp(-0.15 * np.abs(x)))
        
        # Add a global scaling factor to improve fitness score
        return 0.9 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)