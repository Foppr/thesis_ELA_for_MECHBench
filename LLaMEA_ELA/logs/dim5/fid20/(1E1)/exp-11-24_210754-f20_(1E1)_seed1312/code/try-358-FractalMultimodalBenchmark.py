import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced chaotic sine waves with fractal-like interaction terms
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 40.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.6))
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.8) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Increased polynomial corruption with higher-order terms and fractional powers
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.4 + 0.7 * x**3.8 + 0.4 * x**2.7) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Enhanced fractal-like self-similarity through recursive scaling with more complex frequency components
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with stronger asymmetric coupling and modified interaction strengths
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and altered scaling
        f7 = 0.15 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness and discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8