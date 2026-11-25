import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with increased chaos and interaction
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased frequency modulation with chaotic scaling factors
            freq = 40.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Enhanced chaotic behavior with higher-order nonlinear terms
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Modified polynomial corruption with stronger nonlinearity and varied exponents
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.1 + 0.7 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Enhanced saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(8.0 * x))
        
        # Increased fractal self-similarity with higher frequency components and stronger coupling
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Enhanced cross-term interactions with more complex asymmetric coupling
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Modified fractional Brownian motion-like roughness with increased variance and sharper transitions
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Enhanced asymmetric saddle points with stronger curvature and improved nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8