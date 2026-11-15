import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2) / self.dim
        
        # Fractal-like structure using nested trigonometric functions with varying frequencies
        f2 = 0.5 * np.sum(np.sin(10.0 * np.sin(5.0 * x)) * np.cos(8.0 * np.cos(3.0 * x)))
        
        # Polynomial chaos expansion with mixed monomials and trigonometric terms
        f3 = 0.3 * np.sum((x**3 + 0.5 * x**4 + 0.1 * x**5) * np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Adaptive gradient modulation with exponential decay and sinusoidal perturbations
        f4 = 0.2 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Multi-scale interaction terms with fractional powers and logarithmic scaling
        f5 = 0.25 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.log(1.0 + np.abs(x)))
        
        # Saddle point generator with hyperbolic tangent and polynomial coupling
        f6 = 0.15 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.sin(7.0 * x))
        
        # Nested chaotic modulation with recursive trigonometric components
        f7 = 0.1 * np.sum(np.sin(np.sin(np.sin(4.0 * x))) * np.cos(np.cos(np.cos(3.0 * x))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7