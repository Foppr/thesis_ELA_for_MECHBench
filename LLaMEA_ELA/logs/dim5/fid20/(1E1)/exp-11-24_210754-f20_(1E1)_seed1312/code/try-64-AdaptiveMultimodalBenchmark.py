import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying exponents
        f1 = np.sum((x**3.2 + 0.8 * x**2.5 + 0.4 * x**1.7) / self.dim)
        
        # Trigonometric modulations with adaptive frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 25.0 * (1.0 + 0.3 * np.sin(i * 0.7)) * (1.0 + 0.2 * np.cos(i * 0.4))
            amp = 1.0 + 0.5 * np.sin(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Exponential decay with sinusoidal oscillations
        f3 = 0.15 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Multiscale fractal-like structure using recursive transformations
        f4 = 0.1 * np.sum(np.sin(30.0 * np.sin(5.0 * x)) * np.cos(20.0 * np.cos(4.0 * x)))
        
        # Cross-dimensional interaction terms with asymmetric coupling
        f5 = 0.075 * np.sum((x[:-1] * x[1:]**1.3 + 0.6 * x[1:] * x[:-1]**1.1) / self.dim)
        
        # Asymmetric saddle points with varying curvature and nonlinearity
        f6 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.8 + 0.2 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Fractional Brownian motion inspired roughness with variable Hurst parameter
        f7 = 0.05 * np.sum(np.abs(x)**1.3 * np.sin(20.0 * x))
        
        # Combined fitness function with weighted components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7