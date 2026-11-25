import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with higher frequency chaos
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased chaotic scaling with fractional frequencies
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Enhanced fractal modulation with multiple nested nonlinearities
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(20.0 * xi**3)
            f2 += mod**2
        
        # Stronger polynomial corruption with higher-order fractional powers
        f3 = 0.05 * np.sum((x**6.7 + 1.2 * x**5.4 + 0.9 * x**3.8 + 0.6 * x**2.5 + 0.3 * x**1.9) / self.dim)
        
        # Complex saddle point structure with multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tan(0.5 * x))
        
        # Introduce enhanced fractal self-similarity with recursive scaling
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.exp(-0.1 * x**2))
        
        # Stronger cross-term interactions with asymmetric coupling and higher-order terms
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - x[1:]) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Increased fractional Brownian motion-like roughness with higher variance
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Enhanced asymmetric saddle points with variable curvature and nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)) * np.sin(5.0 * x))
        
        # Add additional chaotic interference terms
        f9 = 0.04 * np.sum(np.sin(30.0 * x**2) * np.cos(25.0 * x**3) * np.exp(-0.25 * np.abs(x)))
        
        # Combine all components with adjusted weights for maximum fitness complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9