import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal structure with exponentially increasing frequencies and chaotic scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponentially increasing frequency with chaotic modulation
            freq = 50.0 * np.exp(0.3 * i) * (1.0 + 0.5 * np.sin(i * 0.7))
            # Multi-scale chaotic behavior with fractional powers and exponential decay
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.7) * np.exp(-0.3 * np.abs(xi)**1.3)
            f2 += mod**2
        
        # Polynomial corruption with higher-order terms and fractional exponents
        f3 = 0.05 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.8 + 0.3 * x**2.6) / self.dim)
        
        # Saddle point structure with enhanced exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Fractal-like self-similarity through recursive scaling with extremely high frequency components
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher-order interference
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and higher frequency
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and fractal scaling
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)**1.2))
        
        # Add a novel chaotic component with time-varying parameters and enhanced ruggedness
        f9 = 0.18 * np.sum(np.sin(40.0 * np.sin(20.0 * x)) * np.cos(30.0 * np.cos(15.0 * x)) * np.exp(-0.25 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9