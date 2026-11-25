import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal self-similarity with irregular frequency scaling and chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Irregular frequency scaling based on chaotic sequence and dimension index
            freq = 40.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.sin(i * 0.4))
            # Multi-scale chaotic modulation with exponential decay and irregular phase shifts
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.1) * np.exp(-0.3 * np.abs(xi)) * np.sin(0.5 * xi**3)
            f2 += mod**2
        
        # Polynomial corruption with fractional powers and randomized coefficients for increased complexity
        f3 = 0.04 * np.sum((x**5.5 + 0.9 * x**4.7 + 0.6 * x**3.2 + 0.3 * x**2.4 + 0.1 * x**1.8) / self.dim)
        
        # Saddle point structure with multi-scale interference and asymmetric curvature
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.tanh(0.2 * x))
        
        # Fractal-like recursive scaling with higher harmonic components and irregular coupling
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)) * np.exp(-0.1 * x**2))
        
        # Enhanced cross-term interactions with non-symmetric coupling and irregular phase shifts
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:] + 0.3 * np.sin(i)) * np.cos(1.2 * x[:-1] - x[1:] + 0.4 * np.cos(i)))
        
        # Fractional Brownian motion-like roughness with variable Hurst exponent and increased nonlinearity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and irregular modulation
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.5 - 0.5 * x**2.3 + 0.2 * x) * np.exp(-0.15 * np.abs(x)) * np.sin(0.3 * x**2))
        
        # Add a novel chaotic term with irregular coupling and fractal-like behavior
        f9 = 0.1 * np.sum(np.sin(60.0 * np.sin(20.0 * x)) * np.cos(50.0 * np.cos(15.0 * x)) * np.exp(-0.2 * np.abs(x)) * np.tanh(x))
        
        # Combine all components with adjusted weights for improved fitness and complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9