import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal structure using Chebyshev polynomials with varying degrees
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive degree based on dimension and chaotic scaling
            degree = int(15.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.4)))
            # Chebyshev polynomial with modified interaction terms
            Tn = np.cos(degree * np.arccos(np.clip(xi / 5.0, -1.0, 1.0)))
            mod = Tn * np.exp(-0.3 * np.abs(xi)) * np.sin(20.0 * xi)
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients and fractional powers
        f3 = 0.04 * np.sum((x**5.3 + 0.9 * x**4.7 + 0.6 * x**3.2 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(8.0 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Add cross-term interactions with asymmetric coupling and increased nonlinearity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Introduce fractional Brownian motion-like roughness with increased variance
        f7 = 0.15 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.5 - 0.5 * x**2) * np.exp(-0.15 * np.abs(x)))
        
        # Add a novel component with chaotic modulation and higher-order interactions
        f9 = 0.1 * np.sum(np.sin(30.0 * x + 0.5 * np.sin(50.0 * x)) * np.cos(25.0 * x**2))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9