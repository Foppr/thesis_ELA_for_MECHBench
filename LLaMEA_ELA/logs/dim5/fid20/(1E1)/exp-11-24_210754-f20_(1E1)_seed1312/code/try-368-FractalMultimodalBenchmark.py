import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal self-similarity with multiple nested scales
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale frequency modulation with chaotic scaling
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(i * 0.4))
            # Complex fractal modulation with multiple trigonometric components
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.tan(freq * xi**1.5) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Higher-order polynomial corruption with fractional powers and variable coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.6 * x**3.8 + 0.4 * x**2.3) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tan(5.0 * x))
        
        # Fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)) * np.tan(30.0 * np.sin(8.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher-order terms
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.95 * x[1:]) * np.cos(1.2 * x[:-1] - 1.1 * x[1:]) * np.tan(0.8 * x[:-1] + 0.7 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and complex scaling
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and mixed powers
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.7 + 0.3 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Additional chaotic modulation with time-varying parameters
        f9 = 0.1 * np.sum(np.sin(60.0 * np.sin(20.0 * x)) * np.cos(40.0 * np.cos(15.0 * x)) * np.tan(30.0 * np.sin(10.0 * x)))
        
        # Combined fitness with adjusted weights for enhanced discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9