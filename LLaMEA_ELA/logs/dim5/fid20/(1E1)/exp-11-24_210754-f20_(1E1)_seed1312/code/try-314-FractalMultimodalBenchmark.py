import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Hyperchaotic sinusoidal modulations with nested fractal behavior
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Hyperchaotic frequency modulation using multiple sine/cosine components
            freq = 40.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.9)) * (1.0 + 0.2 * np.sin(i * 0.4))
            # Multi-scale chaotic modulation with fractional powers
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.7) * np.exp(-0.3 * np.abs(xi)**0.8)
            f2 += mod**2
        
        # Enhanced polynomial corruption with higher-order terms and variable exponents
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and enhanced exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity through recursive scaling with higher frequency components and asymmetry
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)) * np.exp(-0.15 * np.abs(x)))
        
        # Cross-term interactions with asymmetric coupling and enhanced nonlinearity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and multi-scale behavior
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and fractal-like scaling
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.12 * np.abs(x)**0.9))
        
        # Add a hyperchaotic component with nested self-similarity and increased complexity
        f9 = 0.1 * np.sum(np.sin(60.0 * np.sin(20.0 * x)) * np.cos(50.0 * np.cos(15.0 * x)) * np.sin(30.0 * x**1.5))
        
        # Combine all components with adjusted weights for improved fitness and discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9