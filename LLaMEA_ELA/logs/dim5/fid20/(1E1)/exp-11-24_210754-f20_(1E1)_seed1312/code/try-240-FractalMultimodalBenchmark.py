import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with exponential frequency growth
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponentially increasing frequency with chaotic scaling
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * np.exp(0.3 * i)
            # Chaotic modulation with higher-order nonlinearities
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.5) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Increased polynomial corruption with fractional powers and enhanced nonlinearity
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**4.1 + 0.6 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Stronger fractal-like self-similarity through recursive scaling with ultra-high frequency components
        f5 = 0.35 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)))
        
        # Enhanced cross-term interactions with asymmetric coupling and higher-order terms
        f6 = 0.1 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.5 * x[:-1] - 1.2 * x[1:]))
        
        # Increased fractional Brownian motion-like roughness with higher variance
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # More complex asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)))
        
        # Add a chaotic component with recursive fractal structure
        f9 = 0.12 * np.sum(np.sin(80.0 * np.sin(20.0 * x)) * np.cos(70.0 * np.cos(15.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9