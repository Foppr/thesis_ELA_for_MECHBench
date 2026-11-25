import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal self-similarity with exponential frequency growth
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponentially increasing frequency with chaotic modulation
            freq = 50.0 * np.exp(0.3 * i) * (1.0 + 0.5 * np.sin(i * 0.7))
            # Multi-scale chaotic interaction with fractional powers
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.7) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Polynomial corruption with higher-order terms and variable coefficients
        f3 = 0.05 * np.sum((x**6.2 + 0.9 * x**5.8 + 0.7 * x**4.1 + 0.5 * x**3.3 + 0.3 * x**2.7) / self.dim)
        
        # Saddle point structure with multi-scale exponential decay and interference
        f4 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Fractal-like self-similarity with recursive scaling and higher frequency components
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)))
        
        # Enhanced cross-term interactions with asymmetric coupling and higher-order terms
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and nonlinearity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with enhanced nonlinearity and variable curvature
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)))
        
        # Add a chaotic noise component with dynamic amplitude scaling
        noise = 0.03 * np.sum(np.sin(100.0 * x + np.random.rand()) * np.cos(80.0 * x))
        
        # Combine all components with adjusted weights for increased fitness complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + noise