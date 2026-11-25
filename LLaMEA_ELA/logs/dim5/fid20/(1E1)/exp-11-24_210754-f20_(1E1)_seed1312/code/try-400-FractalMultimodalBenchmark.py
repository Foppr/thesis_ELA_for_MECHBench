import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal structure with adaptive coupling and chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive frequency with enhanced chaotic scaling
            freq = 40.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6))
            # Chaotic modulation using multi-scale sine-cosine interactions
            mod = np.sin(freq * xi) * np.cos(freq * xi**1.8) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Increased nonlinearity with fractional powers and enhanced polynomial corruption
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.1 + 0.7 * x**3.8 + 0.4 * x**2.6) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal self-similarity through nested trigonometric interactions with higher harmonics
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and enhanced coupling strength
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.85 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased variance and modified scaling
        f7 = 0.12 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with varying curvature and enhanced nonlinearity
        f8 = 0.18 * np.sum((x**4.1 + 0.7 * x**3.2 - 0.5 * x) * np.exp(-0.12 * np.abs(x)))
        
        # Additional fractal coupling term for increased multimodality
        f9 = 0.05 * np.sum(np.sin(30.0 * x) * np.cos(20.0 * x**1.5) * np.exp(-0.25 * np.abs(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9