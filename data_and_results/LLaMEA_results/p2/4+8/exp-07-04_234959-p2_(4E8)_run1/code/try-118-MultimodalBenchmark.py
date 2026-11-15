import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum with enhanced chaotic offset
        self.global_min = np.array([(-1)**i * 2.5 + 0.7 * np.sin(i * np.pi / 3) + 0.3 * np.cos(i * np.pi / 5) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced adaptive scaling and chaotic modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(x) * np.cos(0.5 * x)))
        
        # Enhanced sinusoidal modulations with chaotic frequency progression and coupling
        f2 = np.sum(np.sin(7.0 * x + np.cos(2.0 * x)) * np.cos(4.0 * x + np.sin(1.5 * x)) * np.exp(-0.05 * x**2))
        
        # Higher-order polynomial interactions with cross-terms and chaotic coupling
        f3 = np.sum(x**6 - 20 * x**4 + 100 * x**2 - 50 * np.sin(x))
        
        # Exponential penalty with logarithmic and hyperbolic scaling
        f4 = np.sum(np.exp(0.4 * np.abs(x)) - 1 - 0.3 * np.log(1 + np.abs(x)) - 0.1 * np.tanh(x))
        
        # Chaotic component using nested sine and cosine with dynamic scaling
        f5 = np.sum(np.sin(np.cos(x * np.sin(x))) + np.cos(np.sin(x * np.cos(x))))
        
        # Additional chaotic coupling term with modified interaction and dynamic weights
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.7 * x) * np.exp(-0.15 * x**2))
        
        # Introduce a new chaotic interaction term with dynamic coupling and hyperbolic components
        f7 = np.sum(np.sinh(x * np.sin(x)) * np.cosh(x * np.cos(x)) * np.exp(-0.08 * x**2))
        
        # Introduce a novel cross-dimensional coupling with fractal-like behavior
        f8 = np.sum(np.sin(np.pi * x / 2) * np.cos(np.pi * x / 3) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all components with varying weights and chaotic scaling
        return 0.12 * f1 + 0.20 * f2 + 0.18 * f3 + 0.14 * f4 + 0.08 * f5 + 0.11 * f6 + 0.07 * f7 + 0.10 * f8