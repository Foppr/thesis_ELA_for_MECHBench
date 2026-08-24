import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position with perturbation
        self.global_min = np.array([(-1)**i * 2.0 + 0.5 * np.sin(i) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f1 = np.sum((x - self.global_min)**2 * (1.0 + 0.1 * np.abs(x)))
        
        # Enhanced sinusoidal modulations with chaotic frequency interactions
        f2 = np.sum(np.sin(5.0 * x + np.sin(x)) * np.cos(3.0 * x + np.cos(x)))
        
        # Polynomial interaction with dynamic exponents
        f3 = np.sum((x**4 - 12 * x**2 + 36) * (1.0 + 0.05 * np.sin(2.0 * x)))
        
        # Exponential penalty with variable base
        f4 = np.sum((np.exp(0.3 * np.abs(x)) - 1.0) * (1.0 + 0.1 * np.cos(x)))
        
        # Chaotic component using nested sine functions with phase shifts
        f5 = np.sum(np.sin(np.sin(np.sin(x))) + 0.5 * np.sin(2.0 * x))
        
        # Additional chaotic cross-term interactions to increase complexity
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)))
        
        # Combine all components with optimized weights
        return 0.12 * f1 + 0.30 * f2 + 0.18 * f3 + 0.22 * f4 + 0.10 * f5 + 0.08 * f6