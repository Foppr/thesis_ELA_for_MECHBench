import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal-like global minimum position with recursive chaotic offset
        self.global_min = np.array([(-1)**i * (2.5 + 0.3 * np.sin(i * np.pi / 3)) + 0.2 * np.sin(i * np.pi / 7) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with fractal scaling and adaptive noise
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(x * 2.0)))
        
        # Augmented sinusoidal modulations with fractal frequency progression
        f2 = np.sum(np.sin(7.0 * x + np.cos(2.0 * x)) * np.cos(4.0 * x + np.sin(1.5 * x)))
        
        # Higher-order polynomial interactions with chaotic cross-terms
        f3 = np.sum(x**6 - 20 * x**4 + 100 * x**2 - 50)
        
        # Exponential penalty with fractal logarithmic scaling
        f4 = np.sum(np.exp(0.4 * np.abs(x)) - 1 - 0.3 * np.log(1 + np.abs(x)) + 0.05 * np.sin(x * 3.0))
        
        # Fractal component using nested sine and cosine with recursive scaling
        f5 = np.sum(np.sin(np.cos(np.sin(x))) + np.cos(np.sin(np.cos(x))))
        
        # Additional fractal coupling term with chaotic interaction
        f6 = np.sum(np.sin(x * np.cos(x * 0.5)) * np.cos(x * np.sin(x * 0.7)))
        
        # Combine all components with varying weights and fractal scaling
        return 0.12 * f1 + 0.22 * f2 + 0.18 * f3 + 0.25 * f4 + 0.15 * f5 + 0.08 * f6