import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested sinusoidal modulations with fractal-like behavior and increased chaos
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Highly chaotic frequency modulation using multiple sine/cosine interactions
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(i * 0.4))
            # Chaotic modulation with fractional scaling and exponential decay
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi)**1.3)
            f2 += mod**2
        
        # Add polynomial corruption with higher-order terms and fractional powers
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.8 + 0.3 * x**2.6) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Add cross-term interactions with asymmetric coupling and higher-order nonlinearities
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:] + 0.2 * x[:-1]**2) * np.cos(1.2 * x[:-1] - x[1:] + 0.3 * x[1:]**2))
        
        # Introduce fractional Brownian motion-like roughness with increased variance and chaos
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and fractional derivatives
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)**1.2))
        
        # Introduce chaotic phase shifts and additional interference terms
        f9 = 0.1 * np.sum(np.sin(30.0 * x + 0.5 * np.sin(20.0 * x)) * np.cos(25.0 * x + 0.4 * np.cos(18.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9