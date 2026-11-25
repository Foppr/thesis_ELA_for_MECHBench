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
            # Highly adaptive frequency based on dimension and chaotic scaling with exponential growth
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 1.2)) * (1.0 + 0.5 * np.cos(i * 0.8)) * np.exp(0.1 * i)
            # Chaotic modulation using logistic map-like behavior with fractional scaling and higher harmonics
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(5.0 * xi**3)
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients, fractional powers, and exponential terms
        f3 = 0.04 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**3.8 + 0.6 * x**2.5 + 0.3 * x**1.8) / self.dim)
        
        # Saddle point structure with exponential decay, multi-scale interference, and enhanced nonlinearity
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tanh(2.0 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components and chaotic coupling
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)) * np.exp(-0.1 * x**2))
        
        # Add cross-term interactions with asymmetric coupling and higher-order interference
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - x[1:]) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Introduce fractional Brownian motion-like roughness with increased variance and higher-order terms
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(8.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and complex fractional interactions
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)) * np.sin(3.0 * x))
        
        # Additional chaotic interference with multi-scale harmonic components and increased complexity
        f9 = 0.18 * np.sum(np.sin(60.0 * x + 0.5 * np.sin(20.0 * x)) * np.cos(40.0 * x) * np.exp(-0.25 * x**3))
        
        # Combine all components with adjusted weights for improved fitness and enhanced discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9