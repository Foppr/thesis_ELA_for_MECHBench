import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested trigonometric terms with varying frequencies and modulations
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Nested sine and cosine with increasing complexity
            freq1 = 2.0 * (i + 1)
            freq2 = 3.0 * (i + 1) ** 1.5
            freq3 = 5.0 * (i + 1) ** 0.7
            term = np.sin(freq1 * xi) * np.cos(freq2 * xi**2) * np.sin(freq3 * xi**3)
            f2 += term**2
        
        # Polynomial corruption with fractional exponents
        f3 = 0.05 * np.sum((x**3.7 + 0.7 * x**2.3 + 0.4 * x**1.9) / self.dim)
        
        # Exponential decay with oscillatory modulation
        f4 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(8.0 * x) * np.sin(5.0 * x))
        
        # Saddle point structure with asymmetric coupling
        f5 = 0.2 * np.sum((x**4.1 - 0.8 * x**3.2 + 0.3 * x**2.1) * np.exp(-0.3 * np.abs(x)))
        
        # Cross-term interactions with varying coupling strengths
        f6 = 0.1 * np.sum(np.sin(0.5 * (x[:-1] + x[1:])) * np.cos(0.7 * (x[:-1] - x[1:])))
        
        # Fractional Brownian motion-like roughness
        f7 = 0.15 * np.sum(np.abs(x)**1.3 * np.cos(15.0 * x))
        
        # Asymmetric multimodal structure with multiple peaks
        f8 = 0.25 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.exp(-0.2 * x**2))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8