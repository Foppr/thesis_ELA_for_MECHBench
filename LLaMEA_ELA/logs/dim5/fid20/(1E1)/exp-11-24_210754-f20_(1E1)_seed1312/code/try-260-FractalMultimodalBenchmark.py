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
            # Highly adaptive frequency based on dimension and chaotic scaling
            freq = 50.0 * (1.0 + 0.8 * np.sin(i * 1.2)) * (1.0 + 0.6 * np.cos(i * 0.7))
            # Chaotic modulation using multi-layered logistic map-like behavior with fractional scaling
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(10.0 * xi)
            f2 += mod**2
        
        # Enhanced polynomial corruption with higher-order terms and fractional powers
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**4.8 + 0.6 * x**3.9 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with exponential decay, multi-scale interference, and enhanced nonlinearity
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.tan(0.5 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components and multi-scale coupling
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)) * np.exp(-0.1 * x**2))
        
        # Add cross-term interactions with asymmetric coupling and enhanced coupling strength
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.3 * x[:-1] - x[1:]) * np.exp(-0.2 * np.abs(x[:-1])))
        
        # Introduce fractional Brownian motion-like roughness with increased variance and irregularity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and irregular modulation
        f8 = 0.2 * np.sum((x**4.5 + 0.7 * x**3.6 - 0.5 * x**2.2) * np.exp(-0.15 * np.abs(x)) * np.sin(8.0 * x))
        
        # Add novel irregular polynomial component with variable exponents and cross-dimension coupling
        f9 = 0.04 * np.sum((x**3.3 + 0.4 * x**2.7 + 0.2 * x**1.9) * np.cos(5.0 * x) * np.exp(-0.25 * x**2))
        
        # Combine all components with adjusted weights for improved fitness and increased complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9