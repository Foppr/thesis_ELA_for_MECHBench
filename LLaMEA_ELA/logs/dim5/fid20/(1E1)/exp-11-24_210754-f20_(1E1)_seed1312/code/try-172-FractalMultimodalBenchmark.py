import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Hyperchaotic sinusoidal modulations with higher frequency components
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic scaling with multiple frequency sources
            freq = 45.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(i * 0.4))
            # Multi-scale chaotic modulation with fractional exponents
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.8) * np.exp(-0.3 * np.abs(xi)**0.7)
            f2 += mod**2
        
        # Enhanced polynomial corruption with higher-order terms and variable coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.3 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and enhanced exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity through recursive scaling with more complex frequency interactions
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Enhanced cross-term interactions with non-symmetric coupling and increased complexity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and higher fractional powers
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity using fractional exponents
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)**0.9))
        
        # Add a new component: multi-scale Gaussian-like interference with enhanced fractal properties
        f9 = 0.1 * np.sum(np.exp(-0.5 * (x**2)) * np.sin(30.0 * x) * np.cos(20.0 * x))
        
        # Combine all components with adjusted weights for improved fitness and discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9