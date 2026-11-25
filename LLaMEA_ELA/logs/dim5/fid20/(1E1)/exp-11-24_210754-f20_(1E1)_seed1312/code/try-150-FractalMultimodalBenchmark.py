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
            # Increased chaotic scaling and frequency modulation
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Enhanced fractal behavior with double chaotic modulation
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(20.0 * xi)
            f2 += mod**2
        
        # Increased polynomial corruption with higher degree terms and fractional powers
        f3 = 0.05 * np.sum((x**6.2 + 1.1 * x**5.7 + 0.9 * x**4.8 + 0.6 * x**3.9 + 0.3 * x**2.5) / self.dim)
        
        # Enhanced saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.sin(25.0 * x))
        
        # Stronger fractal-like self-similarity with multiple recursive scaling levels
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.sin(40.0 * x))
        
        # Enhanced cross-term interactions with stronger asymmetric coupling
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 1.1 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[:-1])))
        
        # Increased fractional Brownian motion-like roughness with higher variance
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # More complex asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.7) * np.exp(-0.15 * np.abs(x)) * np.sin(30.0 * x))
        
        # Add additional high-frequency noise component
        f9 = 0.04 * np.sum(np.sin(100.0 * x) * np.cos(80.0 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9