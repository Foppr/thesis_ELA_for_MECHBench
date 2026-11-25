import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested fractal sinusoidal modulations with chaotic scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic frequency modulation using multiple trigonometric components
            freq = 45.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(i * 0.4))
            # Multi-scale chaotic modulation with fractional powers
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi**1.5))
            f2 += mod**2
        
        # Increased polynomial corruption with higher-order terms and variable coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.8 + 0.6 * x**3.9 + 0.4 * x**2.3) / self.dim)
        
        # Enhanced saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tan(0.5 * x))
        
        # Stronger fractal self-similarity through recursive scaling with higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)) * np.exp(-0.15 * np.abs(x)))
        
        # Complex cross-term interactions with asymmetric coupling and higher-order mixing
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:] + 0.3 * x[:-1]**2) * np.cos(1.2 * x[:-1] - x[1:] + 0.4 * x[1:]**2))
        
        # Fractional Brownian motion-like roughness with increased variance and multi-scale features
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and higher-order terms
        f8 = 0.2 * np.sum((x**4.5 + 0.7 * x**3.8 - 0.5 * x**2.7 + 0.3 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Additional chaotic interference terms with nested logarithmic scaling
        f9 = 0.1 * np.sum(np.log(1.0 + 0.5 * np.abs(x)) * np.sin(30.0 * x**2) * np.cos(20.0 * x**1.5))
        
        # Combined components with adjusted weights for superior benchmark discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9