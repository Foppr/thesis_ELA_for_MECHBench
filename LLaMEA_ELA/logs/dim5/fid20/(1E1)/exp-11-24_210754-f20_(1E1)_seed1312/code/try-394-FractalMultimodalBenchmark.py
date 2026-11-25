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
            freq = 40.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.6))
            # Chaotic modulation using logistic map-like behavior with fractional scaling
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients and fractional powers
        f3 = 0.04 * np.sum((x**5.3 + 0.9 * x**4.1 + 0.6 * x**2.7 + 0.3 * x**2.3) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(8.0 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Add cross-term interactions with asymmetric coupling (modified for better discrimination)
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Introduce fractional Brownian motion-like roughness with increased variance
        f7 = 0.15 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8