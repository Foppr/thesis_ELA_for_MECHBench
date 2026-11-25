import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic oscillatory components with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 40.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.4))
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.8) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Enhanced polynomial corruption with higher-order terms and fractional exponents
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Multi-scale saddle point structure with exponential decay and asymmetric interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal self-similarity through nested trigonometric functions with recursive scaling
        f5 = 0.2 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(9.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher frequency components
        f6 = 0.07 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased nonlinearity
        f7 = 0.12 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.18 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Additional chaotic modulation with time-varying parameters
        f9 = 0.08 * np.sum(np.sin(30.0 * x + 0.5 * np.sin(20.0 * x)) * np.cos(25.0 * x**1.5))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9