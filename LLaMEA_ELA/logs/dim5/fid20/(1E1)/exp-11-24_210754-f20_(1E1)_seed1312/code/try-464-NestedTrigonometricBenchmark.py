import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.3 * np.sum(x**2) / self.dim
        
        # Nested sine waves with increasing frequency and amplitude
        f2 = 0.4 * np.sum(np.sin(2.0 * x) + 0.5 * np.sin(4.0 * x) + 0.2 * np.sin(8.0 * x))
        
        # Adaptive frequency modulation based on position
        adaptive_freq = 1.0 + 0.5 * np.abs(x)
        f3 = 0.3 * np.sum(np.sin(adaptive_freq * x) * np.cos(adaptive_freq * x / 2.0))
        
        # Gradient-based attraction fields with exponential decay
        f4 = 0.25 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Cross-dimensional coupling with polynomial interaction
        f5 = 0.2 * np.sum((x[:-1]**2 + x[1:]**2) * np.sin(x[:-1] * x[1:]))
        
        # Multi-scale harmonic interference with phase shifts
        f6 = 0.18 * np.sum(np.sin(15.0 * x + np.cos(7.0 * x)) * np.cos(12.0 * x + np.sin(8.0 * x)))
        
        # Asymmetric polynomial with logarithmic weighting
        f7 = 0.22 * np.sum((x**3.2 + 0.8 * x**2.5 + 0.4 * x**1.8) / self.dim * np.log(1.0 + np.abs(x)))
        
        # Fractal-like pattern with recursive sine-cosine combinations
        f8 = 0.15 * np.sum(np.sin(np.sin(3.0 * x)) * np.cos(np.cos(2.0 * x)))
        
        # Combine all components with varying weights for complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8