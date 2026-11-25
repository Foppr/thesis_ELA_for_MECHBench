import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Highly oscillatory fractal modulations with asymmetric scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric frequency scaling with chaotic modulation
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Multi-scale chaotic interaction with fractional powers
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi)**1.3)
            f2 += mod**2
        
        # Enhanced polynomial corruption with asymmetric fractional exponents
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.6 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale exponential interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity with increased frequency and chaotic coupling
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher-order interference
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.85 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased nonlinearity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with enhanced curvature and chaotic scaling
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)**1.2))
        
        # Additional chaotic interference with multi-scale resonance
        f9 = 0.1 * np.sum(np.sin(60.0 * x) * np.cos(45.0 * x) * np.exp(-0.25 * np.abs(x)**1.5))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9