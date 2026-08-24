import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum position with chaotic offset
        self.global_min = np.array([(-1)**i * 2.5 + 0.5 * np.sin(i * np.pi / 4) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.1 * np.sin(x)))
        
        # Enhanced sinusoidal modulations with chaotic frequency progression
        f2 = np.sum(np.sin(5.0 * x + np.cos(x)) * np.cos(3.0 * x + np.sin(x)))
        
        # Higher-order polynomial interactions with cross-terms
        f3 = np.sum(x**5 - 15 * x**3 + 50 * x)
        
        # Exponential penalty with logarithmic scaling
        f4 = np.sum(np.exp(0.3 * np.abs(x)) - 1 - 0.2 * np.log(1 + np.abs(x)))
        
        # Chaotic component using nested sine and cosine
        f5 = np.sum(np.sin(np.cos(x)) + np.cos(np.sin(x)))
        
        # Additional chaotic coupling term with modified interaction
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.5 * x))
        
        # Cross-dimensional coupling with chaotic phase shifts
        f7 = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # Combine all components with varying weights and chaotic scaling
        return 0.12 * f1 + 0.22 * f2 + 0.18 * f3 + 0.18 * f4 + 0.12 * f5 + 0.10 * f6 + 0.18 * f7