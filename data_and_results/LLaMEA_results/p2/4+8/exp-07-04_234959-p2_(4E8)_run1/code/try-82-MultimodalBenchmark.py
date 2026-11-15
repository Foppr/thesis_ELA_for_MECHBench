import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum with chaotic and fractal-like positioning
        self.global_min = np.array([(-1)**i * (2.0 + 0.3 * np.sin(i * np.pi / 3)) + 0.2 * np.sin(i * np.pi / 7) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quadratic base with dynamic scaling and chaotic modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(2 * x + np.cos(x))))
        
        # Complex sinusoidal interference with time-varying frequencies and phase shifts
        f2 = np.sum(np.sin(7.0 * x + np.cos(3.0 * x)) * np.cos(4.0 * x + np.sin(2.0 * x)) * np.sin(1.5 * x))
        
        # Higher-order polynomial with chaotic coupling and adaptive exponents
        f3 = np.sum(x**6 - 20 * x**4 + 100 * x**2 + 5 * np.sin(x**3))
        
        # Exponential barrier with logarithmic and hyperbolic scaling
        f4 = np.sum(np.exp(0.5 * np.abs(x)) - 1 - 0.3 * np.log(1 + np.abs(x)) - 0.1 * np.tanh(x))
        
        # Chaotic coupling with nested trigonometric and hyperbolic functions
        f5 = np.sum(np.sin(np.cos(np.sin(x))) + np.cos(np.sin(np.cos(x))) + np.tanh(np.sin(x)))
        
        # Modified interaction terms with fractal-like scaling and multi-scale modulation
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.7 * x) * np.cos(0.3 * x**2))
        
        # Additional chaotic perturbation with non-uniform scaling
        f7 = np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1)) * (1 + 0.1 * np.sin(x**2)))
        
        # Combine all components with chaotic weight adjustments and multi-scale normalization
        return 0.10 * f1 + 0.25 * f2 + 0.15 * f3 + 0.15 * f4 + 0.12 * f5 + 0.13 * f6 + 0.10 * f7