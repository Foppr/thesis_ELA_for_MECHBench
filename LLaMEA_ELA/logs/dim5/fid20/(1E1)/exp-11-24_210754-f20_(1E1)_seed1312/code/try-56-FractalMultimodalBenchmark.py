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
            # Adaptive frequency based on dimension and chaotic scaling
            freq = 25.0 * (1.0 + 0.6 * np.sin(i * 0.7)) * (1.0 + 0.4 * np.cos(i * 0.4))
            # Chaotic modulation using logistic map-like behavior with fractional scaling
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.1 * np.abs(xi))
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients and fractional powers
        f3 = 0.018 * np.sum((x**4.7 + 0.7 * x**3.9 + 0.4 * x**2.9 + 0.15 * x**2.1) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.18 * np.sum(np.exp(-0.25 * np.abs(x)) * np.sin(9.0 * x) * np.cos(4.5 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.15 * np.sum(np.sin(35.0 * np.sin(8.0 * x)) * np.cos(25.0 * np.cos(6.0 * x)))
        
        # Add cross-term interactions with asymmetric coupling (modified)
        f6 = 0.04 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(0.9 * x[:-1] - x[1:]))
        
        # Introduce fractional Brownian motion-like roughness
        f7 = 0.06 * np.sum(np.abs(x)**1.4 * np.sin(15.0 * x))
        
        # Asymmetric saddle points with varying curvature (enhanced)
        f8 = 0.10 * np.sum((x**3.2 + 0.5 * x**2.1 - 0.25 * x) * np.exp(-0.06 * np.abs(x)))
        
        # Combine all components with adaptive weights
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8