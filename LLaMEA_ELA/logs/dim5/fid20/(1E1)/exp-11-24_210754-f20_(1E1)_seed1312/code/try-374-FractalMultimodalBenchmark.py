import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal self-similarity with chaotic neural network interactions
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic frequency modulation with neural-inspired scaling
            freq = 42.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(0.4 * i))
            # Multi-scale chaotic modulation with neural-like feedback
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.tanh(2.0 * xi)
            f2 += mod**2
        
        # Polynomial corruption with fractional powers and neural-style nonlinearity
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**4.1 + 0.5 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Saddle point structure with exponential decay and multi-scale interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.tanh(0.5 * x))
        
        # Fractal-like self-similarity through recursive scaling with higher frequency components
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)) * np.exp(-0.1 * x**2))
        
        # Cross-term interactions with asymmetric coupling and neural-style weights
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.85 * x[1:]) * np.cos(1.2 * x[:-1] - 0.9 * x[1:]) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Fractional Brownian motion-like roughness with increased variance and neural feedback
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and fractal feedback
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.1) * np.exp(-0.15 * np.abs(x)) * np.sin(3.0 * x))
        
        # Novel chaotic interaction terms inspired by dynamical systems and fractal geometry
        f9 = 0.18 * np.sum(np.sin(30.0 * x + 0.5 * np.sin(20.0 * x)) * np.cos(25.0 * x**2) * np.exp(-0.25 * x**2))
        
        # Cross-dimensional coupling with fractional scaling and chaotic feedback
        f10 = 0.12 * np.sum(np.sin(x[:-1] + 0.7 * x[1:] + 0.3 * np.sin(5.0 * x[:-1])) * np.cos(0.8 * x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[1:]))
        
        # Combine all components with adjusted weights for improved fitness and complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10