import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum position with fractal-like chaotic offset
        self.global_min = np.array([(-1)**i * 2.5 + 0.5 * np.sin(i * np.pi / 4) + 0.1 * np.sin(i * np.pi / 2) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling and fractal modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.1 * np.sin(x) * np.cos(0.5 * x)))
        
        # Enhanced sinusoidal modulations with fractal frequency progression
        f2 = np.sum(np.sin(5.0 * x + np.cos(x)) * np.cos(3.0 * x + np.sin(x)) * np.sin(0.7 * x))
        
        # Higher-order polynomial interactions with cross-terms and fractal scaling
        f3 = np.sum(x**5 - 15 * x**3 + 50 * x + 0.05 * x**7)
        
        # Exponential penalty with logarithmic scaling and fractal component
        f4 = np.sum(np.exp(0.3 * np.abs(x)) - 1 - 0.2 * np.log(1 + np.abs(x)) + 0.05 * np.sin(2 * x))
        
        # Chaotic component using nested sine and cosine with fractal phase
        f5 = np.sum(np.sin(np.cos(x)) + np.cos(np.sin(x)) + 0.1 * np.sin(np.cos(2 * x)))
        
        # Additional chaotic coupling term with modified interaction and fractal scaling
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Cross-dimensional coupling with chaotic phase shifts and fractal modulation
        f7 = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * np.sin(0.2 * (x[:-1] + x[1:])))
        
        # Fractal-like self-similarity component with multi-scale modulation
        f8 = np.sum(np.sin(10 * x) * np.cos(5 * x) * np.exp(-0.05 * x**2))
        
        # Combine all components with varying weights and fractal scaling
        return 0.10 * f1 + 0.20 * f2 + 0.15 * f3 + 0.15 * f4 + 0.10 * f5 + 0.08 * f6 + 0.12 * f7 + 0.10 * f8