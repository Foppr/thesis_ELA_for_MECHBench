import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal chaos with recursive trigonometric modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency scaling with chaotic sine-cosine coupling
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.3) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Polynomial corruption with higher-order fractional powers and dynamic coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with multi-scale interference and asymmetric exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Introduce higher frequency fractal self-similarity with complex nested modulation
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and dynamic phase shifts
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:] + 0.2 * np.sin(i)) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased nonlinearity and variance
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature and enhanced chaotic behavior
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Add a global perturbation term to increase landscape complexity
        f9 = 0.1 * np.sum(np.sin(30.0 * x) * np.cos(20.0 * x) * np.exp(-0.2 * x**2))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9