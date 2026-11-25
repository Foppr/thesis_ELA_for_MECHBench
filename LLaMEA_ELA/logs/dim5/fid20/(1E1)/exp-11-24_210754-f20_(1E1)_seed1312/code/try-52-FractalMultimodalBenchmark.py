import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested sinusoidal modulations with fractal-like behavior
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Slightly altered frequency scaling with modified chaotic modulation
            freq = 25.0 * (1.0 + 0.4 * np.sin(i * 0.6)) * (1.0 + 0.2 * np.cos(i * 0.3))
            # Modified chaotic modulation using logistic map-like behavior with fractional scaling
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.15 * np.abs(xi))
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients and fractional powers
        f3 = 0.02 * np.sum((x**4.7 + 0.5 * x**3.9 + 0.25 * x**2.6 + 0.15 * x**1.8) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.2 * np.sum(np.exp(-0.25 * np.abs(x)) * np.sin(9.0 * x) * np.cos(3.5 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.1 * np.sum(np.sin(35.0 * np.sin(6.5 * x)) * np.cos(22.0 * np.cos(4.5 * x)))
        
        # Add cross-term interactions with asymmetric coupling
        f6 = 0.04 * np.sum(np.sin(x[:-1] + 0.6 * x[1:]) * np.cos(0.7 * x[:-1] - x[1:]))
        
        # Introduce fractional Brownian motion-like roughness
        f7 = 0.06 * np.sum(np.abs(x)**1.4 * np.sin(13.0 * x))
        
        # Asymmetric saddle points with varying curvature
        f8 = 0.09 * np.sum((x**3.2 + 0.35 * x**2.1 - 0.15 * x) * np.exp(-0.06 * np.abs(x)))
        
        # Combine all components with adaptive weights
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8