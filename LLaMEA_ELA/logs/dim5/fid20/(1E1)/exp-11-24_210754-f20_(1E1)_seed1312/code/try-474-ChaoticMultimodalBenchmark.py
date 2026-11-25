import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic growth
        f1 = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced exponential decay with trigonometric interference
        f2 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(12.0 * x) * np.cos(8.0 * x))
        
        # Modified polynomial modulation with higher-order terms and asymmetric coefficients
        f3 = 0.2 * np.sum((x**5.0 + 0.6 * x**4.0 + 0.4 * x**3.0 + 0.2 * x**2.0 + 0.1 * x) / self.dim)
        
        # Improved saddle point structure with chaotic sine-cosine coupling
        f4 = 0.25 * np.sum(np.sin(18.0 * x) * np.cos(15.0 * x) * np.exp(-0.25 * x**2))
        
        # Enhanced cross-dimensional interaction with stronger coupling
        f5 = 0.15 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.9 * x[:-1] + 1.1 * x[1:]))
        
        # Strengthened fractal-like recursive interference with multiple scales
        f6 = 0.2 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)))
        
        # Refined asymmetric polynomial with exponential weighting
        f7 = 0.2 * np.sum((x**4.0 + 0.4 * x**3.2 - 0.2 * x**1.8) * np.exp(-0.15 * np.abs(x)))
        
        # Advanced multi-scale harmonic modulation with phase coupling
        f8 = 0.15 * np.sum(np.sin(35.0 * x + np.sin(20.0 * x)) * np.cos(30.0 * x + np.cos(15.0 * x)))
        
        # Additional chaotic interference term for increased complexity
        f9 = 0.1 * np.sum(np.sin(28.0 * x) * np.cos(22.0 * x) * np.sin(16.0 * x))
        
        # Combine all components with optimized weights for better algorithm discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9