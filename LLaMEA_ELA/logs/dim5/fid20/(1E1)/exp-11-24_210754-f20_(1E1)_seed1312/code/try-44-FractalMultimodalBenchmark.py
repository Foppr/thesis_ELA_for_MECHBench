import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested sinusoidal modulations with fractal-like behavior
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive frequency based on dimension
            freq = 10.0 * (1.0 + 0.5 * np.sin(i))
            # Chaotic modulation using logistic map-like behavior
            mod = np.sin(freq * xi) * np.cos(freq * xi**2)
            f2 += mod**2
        
        # Add polynomial corruption with varying coefficients
        f3 = 0.01 * np.sum((x**5 + 0.5 * x**4 + 0.2 * x**3 + 0.05 * x**2) / self.dim)
        
        # Saddle point structure with exponential decay
        f4 = 0.1 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(5.0 * x) * np.cos(2.0 * x))
        
        # Introduce fractal-like self-similarity through recursive scaling
        f5 = 0.05 * np.sum(np.sin(20.0 * np.sin(5.0 * x)) * np.cos(10.0 * np.cos(3.0 * x)))
        
        # Combine all components with adaptive weights
        return f1 + f2 + f3 + f4 + f5