import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested sinusoidal modulations with enhanced fractal behavior
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased chaotic scaling and frequency modulation
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Enhanced chaotic modulation with higher-order nonlinearities
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Stronger polynomial corruption with fractional powers and increased coefficients
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**3.8 + 0.4 * x**3.2) / self.dim)
        
        # Enhanced saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # More complex fractal-like self-similarity with higher frequency components
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(12.0 * x)) * np.cos(45.0 * np.cos(10.0 * x)))
        
        # Stronger cross-term interactions with asymmetric coupling and increased nonlinearity
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Increased fractional Brownian motion-like roughness with higher variance
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # More complex asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.5 + 0.7 * x**3.6 - 0.5 * x**2) * np.exp(-0.15 * np.abs(x)))
        
        # Add additional chaotic interference terms with modified scaling
        f9 = 0.04 * np.sum(np.sin(30.0 * np.cos(5.0 * x)) * np.cos(25.0 * np.sin(6.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness landscape complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9