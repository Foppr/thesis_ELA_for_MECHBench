import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.3 * np.sum(x**2) / self.dim
        
        # Nested trigonometric components with varying frequencies
        f2 = 0.4 * np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Amplitude modulation with exponential decay
        f3 = 0.25 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(7.0 * x) * np.cos(4.0 * x))
        
        # Chaotic logistic map component scaled by dimension
        logistic = np.zeros_like(x)
        r = 3.95
        for _ in range(10):
            logistic = r * logistic * (1 - logistic)
        f4 = 0.2 * np.sum(logistic * np.sin(6.0 * x))
        
        # Multi-scale harmonic interference
        f5 = 0.2 * np.sum(np.sin(10.0 * x + np.sin(8.0 * x)) * np.cos(9.0 * x + np.cos(7.0 * x)))
        
        # Asymmetric polynomial with sine-cosine coupling
        f6 = 0.15 * np.sum((x**3.2 + 0.5 * x**2.7) * np.sin(4.0 * x) * np.cos(2.0 * x))
        
        # Cross-dimensional interaction with nested sinusoids
        f7 = 0.1 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.5 * x[:-1] + 2.0 * x[1:]))
        
        # Fractal-like recursive modulation
        f8 = 0.12 * np.sum(np.sin(15.0 * np.sin(3.0 * x)) * np.cos(12.0 * np.cos(2.5 * x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8