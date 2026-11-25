import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with fractal-like behavior and increased chaos
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Highly adaptive frequency with chaotic scaling and dimension-dependent modulation
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(i * 0.4))
            # Chaotic modulation using multi-scale logistic map behavior with fractional scaling
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(2.0 * xi)
            f2 += mod**2
        
        # Enhanced polynomial corruption with higher-degree terms and increased nonlinearity
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**4.8 + 0.7 * x**3.9 + 0.5 * x**2.8) / self.dim)
        
        # Saddle point structure with exponential decay, multi-scale interference, and enhanced asymmetry
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.tan(0.5 * x))
        
        # Introduce higher-order fractal-like self-similarity through recursive scaling with ultra-high frequency components
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.exp(-0.1 * x**2))
        
        # Enhanced cross-term interactions with asymmetric coupling and multi-scale interference
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - x[1:]) * np.exp(-0.2 * np.abs(x[:-1])))
        
        # Fractional Brownian motion-like roughness with increased variance and multi-scale fractal structure
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(3.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and complex interaction terms
        f8 = 0.2 * np.sum((x**4.5 + 0.7 * x**3.6 - 0.5 * x**2.5 + 0.3 * x) * np.exp(-0.15 * np.abs(x)) * np.sin(3.0 * x))
        
        # Add novel multi-scale Gaussian interference terms for increased complexity
        f9 = 0.1 * np.sum(np.exp(-0.5 * (x - 2.0)**2) * np.sin(50.0 * x) + np.exp(-0.5 * (x + 2.0)**2) * np.cos(40.0 * x))
        
        # Combine all components with adjusted weights for improved fitness and discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9