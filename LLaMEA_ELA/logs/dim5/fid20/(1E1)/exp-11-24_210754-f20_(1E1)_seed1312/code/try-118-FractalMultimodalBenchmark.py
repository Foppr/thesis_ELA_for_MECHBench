import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal self-similarity with asymmetric coupled oscillators
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric coupling with chaotic scaling factors
            freq1 = 42.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            freq2 = 38.0 * (1.0 + 0.6 * np.cos(i * 0.7)) * (1.0 + 0.4 * np.sin(i * 0.8))
            # Multi-scale oscillatory behavior with fractional powers
            mod1 = np.sin(freq1 * xi) * np.cos(freq2 * xi**1.7) * np.exp(-0.3 * np.abs(xi))
            mod2 = np.cos(freq1 * xi**1.3) * np.sin(freq2 * xi) * np.exp(-0.25 * np.abs(xi**1.5))
            f2 += (mod1 + 0.7 * mod2)**2
        
        # Fractional-order polynomial corruption with increased nonlinearity
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.4 + 0.7 * x**3.8 + 0.5 * x**2.7 + 0.3 * x**1.9) / self.dim)
        
        # Saddle point structure with enhanced multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.sin(25.0 * x))
        
        # Fractal-like recursive scaling with higher frequency components and chaos
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)) * np.exp(-0.2 * np.abs(x)))
        
        # Cross-term interactions with asymmetric coupling and fractional powers
        f6 = 0.08 * np.sum(np.sin(0.9 * x[:-1] + 1.1 * x[1:]) * np.cos(1.2 * x[:-1] - 0.8 * x[1:]) * np.abs(x[:-1] - x[1:])**0.7)
        
        # Fractional Brownian motion-like roughness with increased variance and asymmetry
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, fractional dynamics, and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)) * np.sin(5.0 * x))
        
        # Add a new chaotic component with nested exponential decay and fractal coupling
        f9 = 0.18 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(30.0 * np.sin(5.0 * x)) * np.cos(20.0 * np.cos(3.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9