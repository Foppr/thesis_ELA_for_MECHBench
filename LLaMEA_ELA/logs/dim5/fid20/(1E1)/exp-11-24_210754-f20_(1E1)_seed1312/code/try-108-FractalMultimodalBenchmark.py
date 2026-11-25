import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with fractal-like behavior and higher frequency components
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive frequency based on dimension and chaotic scaling with increased complexity
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 1.2)) * (1.0 + 0.5 * np.cos(i * 0.8))
            # Chaotic modulation using logistic map-like behavior with fractional scaling and enhanced nonlinearity
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi)) * np.sin(10.0 * xi)
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients, fractional powers and increased complexity
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**4.8 + 0.6 * x**3.9 + 0.3 * x**2.7) / self.dim)
        
        # Saddle point structure with exponential decay, multi-scale interference and enhanced asymmetry
        f4 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tan(0.5 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components and increased complexity
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Add cross-term interactions with asymmetric coupling and enhanced nonlinearity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - x[1:]) * np.exp(-0.2 * np.abs(x[:-1])))
        
        # Introduce fractional Brownian motion-like roughness with increased variance and enhanced complexity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(5.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity and fractal scaling
        f8 = 0.2 * np.sum((x**4.5 + 0.7 * x**3.8 - 0.5 * x**2.9) * np.exp(-0.15 * np.abs(x)) * np.sin(3.0 * x))
        
        # Add a new component with chaotic tent map behavior and high-frequency oscillations
        f9 = 0.12 * np.sum(np.abs(2.0 * np.mod(x, 1.0) - 1.0) * np.sin(50.0 * x) * np.cos(20.0 * x))
        
        # Combine all components with adjusted weights for improved fitness and enhanced challenge
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9