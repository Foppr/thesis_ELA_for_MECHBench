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
            freq = 37.0 * (1.0 + 0.6 * np.sin(i * 0.85)) * (1.0 + 0.4 * np.cos(i * 0.55))
            # Chaotic modulation using logistic map-like behavior with fractional scaling
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.25 * np.abs(xi))
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients and fractional powers
        f3 = 0.032 * np.sum((x**5.1 + 0.82 * x**4.3 + 0.52 * x**2.9 + 0.26 * x**2.1) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.26 * np.sum(np.exp(-0.37 * np.abs(x)) * np.sin(12.5 * x) * np.cos(7.5 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.26 * np.sum(np.sin(47.0 * np.sin(10.5 * x)) * np.cos(37.0 * np.cos(8.5 * x)))
        
        # Add cross-term interactions with asymmetric coupling (modified for better discrimination)
        f6 = 0.062 * np.sum(np.sin(x[:-1] + 0.92 * x[1:]) * np.cos(1.02 * x[:-1] - x[1:]))
        
        # Introduce fractional Brownian motion-like roughness with increased variance
        f7 = 0.11 * np.sum(np.abs(x)**1.62 * np.sin(20.5 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.17 * np.sum((x**3.95 + 0.62 * x**2.85 - 0.42 * x) * np.exp(-0.11 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8