import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal self-similarity with higher frequency components and chaotic scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased chaotic modulation with multi-scale frequency
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.sin(i * 0.4))
            # Enhanced nonlinear interaction with fractional powers
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Introduce higher-order polynomial corruption with increased nonlinearity
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.8 + 0.3 * x**2.4) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Fractal-like self-similarity with recursive scaling and higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Enhanced cross-term interactions with asymmetric coupling and increased complexity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.95 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[:-1])))
        
        # Fractional Brownian motion-like roughness with increased variance and fractal dimension
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and multi-scale behavior
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)))
        
        # Additional chaotic modulation with time-delayed feedback and enhanced coupling
        f9 = 0.05 * np.sum(np.sin(30.0 * x + 0.8 * np.sin(20.0 * x)) * np.cos(25.0 * x + 0.6 * np.cos(15.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9