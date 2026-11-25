import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with hyperbolic and chaotic behavior
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Hyperbolic frequency scaling with chaotic modulation
            freq = 50.0 * np.tanh(1.5 + 0.8 * np.sin(i * 0.7)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Chaotic modulation using hyperbolic tangent and exponential decay
            mod = np.tanh(freq * xi) * np.exp(-0.3 * np.abs(xi)) * np.sin(freq * xi**1.7)
            f2 += mod**2
        
        # Polynomial corruption with higher-order fractional powers and asymmetric coefficients
        f3 = 0.05 * np.sum((x**6.2 + 0.9 * x**5.4 + 0.7 * x**3.8 + 0.4 * x**2.5 + 0.1 * x**1.9) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tanh(2.0 * x))
        
        # Fractal-like self-similarity with recursive scaling and higher frequency components
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.exp(-0.15 * np.abs(x)))
        
        # Cross-term interactions with asymmetric coupling and hyperbolic sine
        f6 = 0.08 * np.sum(np.sinh(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and hyperbolic scaling
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.tanh(3.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and exponential coupling
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)) * np.tanh(1.5 * x))
        
        # Additional high-frequency chaotic component for increased complexity
        f9 = 0.1 * np.sum(np.sin(100.0 * np.sin(20.0 * x)) * np.cos(80.0 * np.cos(15.0 * x)) * np.exp(-0.2 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9