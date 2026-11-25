import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Sinusoidal modulations with chaotic frequency scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.4))
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.5) * np.exp(-0.1 * np.abs(xi))
            f2 += mod**2
        
        # Polynomial corruption with fractional powers and varying coefficients
        f3 = 0.05 * np.sum((x**4.7 + 0.7 * x**3.8 + 0.4 * x**2.6 + 0.15 * x**1.9) / self.dim)
        
        # Asymmetric saddle points with exponential decay
        f4 = 0.2 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Fractal-like recursive structure with multi-scale interference
        f5 = 0.15 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and varying strength
        f6 = 0.08 * np.sum(np.sin(0.8 * x[:-1] + 1.2 * x[1:]) * np.cos(1.5 * x[:-1] - 0.7 * x[1:]))
        
        # Fractional Brownian motion-like roughness with varying Hurst parameter
        f7 = 0.1 * np.sum(np.abs(x)**1.4 * np.sin(15.0 * x))
        
        # Asymmetric polynomial terms with varying curvature and nonlinearity
        f8 = 0.18 * np.sum((x**3.5 + 0.5 * x**2.4 - 0.3 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Combine all components with adjusted weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8