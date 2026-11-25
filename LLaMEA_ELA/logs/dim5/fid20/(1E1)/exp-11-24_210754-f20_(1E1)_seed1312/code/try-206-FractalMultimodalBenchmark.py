import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal-like structure with irregular frequency modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Irregular chaotic scaling with dynamic frequency based on dimension index
            freq = 45.0 * (1.0 + 0.7 * np.sin(i * 1.1)) * (1.0 + 0.5 * np.cos(i * 0.9)) * (1.0 + 0.3 * np.tan(i * 0.6))
            # Multi-scale chaotic modulation with sine-cosine-product and exponential decay
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(0.5 * freq * xi**3)
            f2 += mod**2
        
        # Polynomial corruption with higher-order terms and fractional powers
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.6 * x**3.8 + 0.4 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.tan(0.3 * x))
        
        # Fractal self-similarity with recursive higher frequency components and asymmetric scaling
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Cross-term interactions with asymmetric coupling and dynamic phase shifts
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:] + 0.2 * np.sin(i * 0.5)) * np.cos(1.2 * x[:-1] - x[1:] + 0.3 * np.cos(i * 0.7)))
        
        # Fractional Brownian motion-like roughness with variable Hölder exponent
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity and multi-modal peaks
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)) * np.sin(2.0 * x))
        
        # Composite chaotic interference with additional sinusoidal modulation
        f9 = 0.1 * np.sum(np.sin(60.0 * x) * np.cos(45.0 * x) * np.exp(-0.2 * np.abs(x)) * np.tan(0.4 * x))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9