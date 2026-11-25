import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Highly oscillatory fractal structure with chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased frequency and chaotic scaling
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Enhanced nonlinearity with fractional powers and exponential decay
            mod = np.sin(freq * xi**1.7) * np.cos(freq * xi**2.3) * np.exp(-0.3 * np.abs(xi)**0.8)
            f2 += mod**2
        
        # Polynomial corruption with higher-order terms and increased nonlinearity
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**4.1 + 0.6 * x**3.4 + 0.3 * x**2.8) / self.dim)
        
        # Multi-scale saddle points with exponential interference
        f4 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.sin(25.0 * x))
        
        # Fractal-like recursive structure with increased complexity
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.exp(-0.4 * np.abs(x)))
        
        # Enhanced cross-term interactions with asymmetric coupling and higher-order mixing
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - 1.2 * x[1:]) * np.exp(-0.1 * np.abs(x[:-1] + x[1:])))
        
        # Fractional Brownian motion with increased roughness and chaotic scaling
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(18.0 * x))
        
        # Asymmetric saddle points with variable curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.6 - 0.5 * x**2.4) * np.exp(-0.15 * np.abs(x)**0.9))
        
        # Additional chaotic interference with fractal-like scaling
        f9 = 0.12 * np.sum(np.sin(35.0 * np.cos(20.0 * x)) * np.cos(40.0 * np.sin(15.0 * x)) * np.exp(-0.25 * np.abs(x)**1.2))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9