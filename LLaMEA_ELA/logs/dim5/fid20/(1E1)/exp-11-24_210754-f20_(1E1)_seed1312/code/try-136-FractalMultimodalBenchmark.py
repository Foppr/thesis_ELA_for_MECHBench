import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal structure with chaotic frequency modulation and discontinuous jumps
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Highly chaotic frequency scaling with jump discontinuities
            freq = 50.0 * (1.0 + 0.8 * np.sin(i * 1.2)) * (1.0 + 0.6 * np.cos(i * 0.9))
            # Multi-scale sinusoidal interference with abrupt phase shifts
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi))
            # Add discontinuous jump terms for increased complexity
            if np.abs(xi) < 1.0:
                mod += 0.5 * np.sin(100.0 * xi**3)
            f2 += mod**2
        
        # Polynomial corruption with fractional powers and irregular coefficients
        f3 = 0.04 * np.sum((x**6.7 + 0.9 * x**5.2 + 0.7 * x**3.8 + 0.4 * x**2.3) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal self-similarity with recursive scaling and higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and non-linear mixing
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[:-1])))
        
        # Fractional Brownian motion-like roughness with enhanced variance and irregular scaling
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and discontinuous derivatives
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Add irregular noise terms to increase optimization difficulty
        noise = 0.05 * np.sum(np.sin(100.0 * x) * np.cos(80.0 * x))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + noise