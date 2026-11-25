import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Hyperchaotic sinusoidal modulations with fractal-like behavior
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic scaling with higher frequency components
            freq = 45.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Hyperchaotic modulation using multi-scale fractional behavior
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Enhanced polynomial corruption with fractional powers and increased complexity
        f3 = 0.04 * np.sum((x**5.5 + 0.9 * x**4.7 + 0.6 * x**3.2 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and enhanced exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Fractal-like self-similarity through recursive scaling with even higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Enhanced cross-term interactions with asymmetric coupling and increased nonlinearity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.95 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with higher variance and complexity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Enhanced asymmetric saddle points with varying curvature and increased nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**2) * np.exp(-0.15 * np.abs(x)))
        
        # Add additional fractal-like component with recursive scaling and multi-scale interference
        f9 = 0.18 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9