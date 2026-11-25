import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal-like structure with recursive scaling and chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased chaos through higher frequency components and fractional scaling
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.3) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Polynomial corruption with higher-order terms and variable coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal self-similarity through nested trigonometric functions with varying scales
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and enhanced coupling strength
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and irregularity
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature and higher-order nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.6 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)))
        
        # Additional chaotic modulation with time-varying parameters
        f9 = 0.1 * np.sum(np.sin(60.0 * x + 0.3 * np.sin(30.0 * x)) * np.cos(50.0 * x + 0.2 * np.cos(25.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness landscape
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9