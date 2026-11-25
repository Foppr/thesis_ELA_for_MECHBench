import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal sinusoidal modulations with fractional chaos
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractional chaotic scaling with varying exponents
            freq = 40.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Multi-scale chaotic modulation with fractional powers
            mod = np.sin(freq * xi**1.3) * np.cos(freq * xi**2.1) * np.exp(-0.3 * np.abs(xi)**0.7)
            f2 += mod**2
        
        # Increased polynomial corruption with higher-order terms and fractional exponents
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.4 + 0.7 * x**3.8 + 0.5 * x**2.5 + 0.3 * x**1.9) / self.dim)
        
        # Saddle point structure with multi-scale interference and enhanced exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Recursive fractal self-similarity with higher frequency components and chaos
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Stronger cross-term interactions with asymmetric coupling and fractional scaling
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.95 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and chaos
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and fractional exponents
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x**1.8) * np.exp(-0.15 * np.abs(x)**0.9))
        
        # Additional chaotic interference terms with higher frequency and complexity
        f9 = 0.1 * np.sum(np.sin(60.0 * x) * np.cos(50.0 * x**1.5) * np.exp(-0.25 * np.abs(x)**1.2))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9