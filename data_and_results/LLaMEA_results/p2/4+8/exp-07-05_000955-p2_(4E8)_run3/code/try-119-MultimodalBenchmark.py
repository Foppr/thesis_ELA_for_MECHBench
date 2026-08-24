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
        f2 = 0.5 * np.sum(np.sin(12.0 * np.sin(4.0 * x)) * np.cos(7.0 * np.cos(2.5 * x)))
        
        # Polynomial chaos expansion with mixed monomials and trigonometric terms
        f3 = 0.35 * np.sum((x**3 + 0.6 * x**4 + 0.12 * x**5) * np.sin(2.5 * x) * np.cos(1.3 * x))
        
        # Adaptive gradient modulation with exponential decay and sinusoidal perturbations
        f4 = 0.22 * np.sum(np.exp(-0.25 * np.abs(x)) * np.sin(14.0 * x) * np.cos(9.0 * x))
        
        # Multi-scale interaction terms with fractional powers and logarithmic scaling
        f5 = 0.28 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.log(1.2 + np.abs(x)))
        
        # Saddle point generator with hyperbolic tangent and polynomial coupling
        f6 = 0.16 * np.sum(np.tanh(x) * (x**2 - 1.2) * np.sin(6.5 * x))
        
        # Nested chaotic modulation with recursive trigonometric components
        f7 = 0.12 * np.sum(np.sin(np.sin(np.sin(3.5 * x))) * np.cos(np.cos(np.cos(2.8 * x))))
        
        # New logarithmic coupling term to increase condition number variation
        f8 = 0.1 * np.sum(np.log(1.0 + 0.5 * np.abs(x)) * np.sin(10.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8