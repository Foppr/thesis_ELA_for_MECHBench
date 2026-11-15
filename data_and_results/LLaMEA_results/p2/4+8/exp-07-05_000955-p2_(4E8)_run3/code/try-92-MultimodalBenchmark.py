import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested trigonometric component with varying frequencies
        f1 = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * np.sin(5.0 * np.pi * x))
        
        # Polynomial chaos expansion with mixed monomials
        f2 = np.sum(x**2 + 0.5 * x**3 + 0.1 * x**4 + 0.05 * x**5)
        
        # Adaptive gradient modulation with dynamic scaling
        grad_mod = np.abs(x) * np.exp(-0.1 * np.abs(x))
        f3 = np.sum(grad_mod * np.sin(4.0 * x) * np.cos(2.0 * x))
        
        # Multi-scale interaction with log-scaled distances and sine modulation
        f4 = np.sum(np.sin(np.log(np.abs(x) + 1.0)) * np.cos(np.log(np.abs(x) + 1.0)))
        
        # Saddle point distribution with hyperbolic and polynomial components
        f5 = np.sum(np.tanh(x) * (x**2 - 1.0) * np.cos(3.0 * x))
        
        # Fractal-like structure using recursive polynomial transformations
        f6 = np.sum((x**2 + 0.1 * x**3) * np.sin(4.0 * x) * np.cos(3.0 * x))
        
        # Cross-term coupling with exponential decay and sinusoidal perturbations
        f7 = np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(8.0 * x) * np.cos(6.0 * x))
        
        # Combine all components with varying weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.25 * f5 + 0.1 * f6 + 0.1 * f7