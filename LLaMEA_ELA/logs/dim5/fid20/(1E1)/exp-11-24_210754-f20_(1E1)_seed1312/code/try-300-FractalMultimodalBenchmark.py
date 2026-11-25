import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Nested exponential decay with fractal scaling and chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency scaling with exponential growth
            freq = 50.0 * np.exp(0.3 * i) * (1.0 + 0.5 * np.sin(i * 0.7))
            # Chaotic sine-cosine modulation with asymmetric decay
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.7) * np.exp(-0.5 * xi**2)
            f2 += mod**2
        
        # Add highly non-uniform polynomial corruption with fractional powers and varying coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**3.8 + 0.4 * x**2.5 + 0.1 * x**1.9) / self.dim)
        
        # Saddle point structure with multi-scale interference and asymmetric exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity through recursive nested trigonometric functions with increased complexity
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher-order nonlinearities
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with higher variance and sharper irregularities
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature, enhanced nonlinearity, and chaotic scaling
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**1.8) * np.exp(-0.15 * np.abs(x)))
        
        # Add a new component: ultra-high frequency chaotic modulation to increase landscape complexity
        f9 = 0.1 * np.sum(np.sin(100.0 * np.sin(20.0 * x)) * np.cos(80.0 * np.cos(15.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness landscape discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9