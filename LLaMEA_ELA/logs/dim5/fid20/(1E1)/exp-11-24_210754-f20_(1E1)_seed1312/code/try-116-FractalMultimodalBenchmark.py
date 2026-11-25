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
            # Highly adaptive frequency based on dimension and chaotic scaling with higher complexity
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 1.1)) * (1.0 + 0.5 * np.cos(i * 0.8)) * (1.0 + 0.3 * np.sin(i * 0.3))
            # Enhanced chaotic modulation using multi-layered logistic map behavior
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(2.0 * freq * np.sin(xi))
            f2 += mod**2
        
        # Increased polynomial corruption with higher degree terms and fractional powers
        f3 = 0.05 * np.sum((x**6.7 + 1.2 * x**5.9 + 0.9 * x**4.8 + 0.6 * x**3.7 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference enhanced
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tan(0.5 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components and chaos
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Enhanced cross-term interactions with asymmetric coupling and higher-order terms
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - x[1:]) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Introduce fractional Brownian motion-like roughness with increased variance and higher fractal dimension
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(3.0 * x))
        
        # Enhanced asymmetric saddle points with varying curvature, enhanced nonlinearity, and multi-scale behavior
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)) * np.sin(5.0 * x))
        
        # Additional high-frequency chaotic component to increase landscape complexity
        f9 = 0.1 * np.sum(np.sin(100.0 * x) * np.cos(80.0 * x**2) * np.exp(-0.25 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness and challenge
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9