import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic sine-wave modulations with fractal-like interaction
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Frequency modulation based on dimension and chaotic scaling
            freq = 40.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.6))
            # Multi-scale sine modulation with exponential decay
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.5) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Polynomial corruption with fractional powers and increased nonlinearity
        f3 = 0.04 * np.sum((x**5.5 + 0.9 * x**4.7 + 0.6 * x**3.2 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and asymmetric curvature
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity through recursive sine-cosine combinations
        f5 = 0.2 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(9.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher-order terms
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with enhanced variance
        f7 = 0.12 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature and increased complexity
        f8 = 0.18 * np.sum((x**4.1 + 0.7 * x**3.4 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)))
        
        # Combine all components with adjusted weights for better discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8