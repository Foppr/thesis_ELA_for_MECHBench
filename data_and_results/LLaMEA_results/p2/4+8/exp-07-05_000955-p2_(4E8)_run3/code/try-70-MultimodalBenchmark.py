import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal-like structure using nested trigonometric functions with varying frequencies
        f2 = 0.7 * np.sum(np.sin(15.0 * np.sin(7.0 * x)) * np.cos(12.0 * np.cos(5.0 * x)))
        
        # Polynomial chaos expansion with mixed monomials and trigonometric terms
        f3 = 0.4 * np.sum((x**4 + 0.6 * x**5 + 0.15 * x**6) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Adaptive gradient modulation with exponential decay and sinusoidal perturbations
        f4 = 0.3 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Multi-scale interaction terms with fractional powers and logarithmic scaling
        f5 = 0.3 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.log(1.0 + 2.0 * np.abs(x)))
        
        # Saddle point generator with hyperbolic tangent and polynomial coupling
        f6 = 0.2 * np.sum(np.tanh(x) * (x**3 - 1.0) * np.sin(9.0 * x))
        
        # Nested chaotic modulation with recursive trigonometric components
        f7 = 0.15 * np.sum(np.sin(np.sin(np.sin(6.0 * x))) * np.cos(np.cos(np.cos(4.0 * x))))
        
        # Additional chaotic interaction terms for increased complexity
        f8 = 0.25 * np.sum(np.sin(2.0 * np.sin(3.0 * x)) * np.cos(1.5 * np.cos(2.5 * x)) * np.sin(0.5 * x**2))
        
        # Cross-dimensional coupling with enhanced non-separability
        f9 = 0.18 * np.sum((x[:-1] + x[1:]) * np.sin(5.0 * (x[:-1] - x[1:])) * np.cos(3.0 * (x[:-1] + x[1:])))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9