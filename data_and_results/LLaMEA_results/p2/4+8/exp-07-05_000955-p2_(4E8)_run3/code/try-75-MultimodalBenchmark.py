import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced chaotic interactions with nested trigonometric functions
        f2 = 0.6 * np.sum(np.sin(12.0 * np.sin(7.0 * x)) * np.cos(9.0 * np.cos(4.0 * x)))
        
        # Modified radial components with polynomial coupling
        f3 = 0.4 * np.sum((x**3 + 0.3 * x**4 + 0.05 * x**5) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Increased polynomial coupling with adaptive scaling
        f4 = 0.3 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Novel adaptive scaling with fractional powers and logarithmic terms
        f5 = 0.2 * np.sum(np.sin(np.power(np.abs(x), 0.7)) * np.cos(np.power(np.abs(x), 0.7)) * np.log(1.0 + np.abs(x)))
        
        # Saddle point generator with hyperbolic tangent and polynomial coupling
        f6 = 0.18 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.sin(9.0 * x))
        
        # Nested chaotic modulation with recursive trigonometric components
        f7 = 0.12 * np.sum(np.sin(np.sin(np.sin(5.0 * x))) * np.cos(np.cos(np.cos(4.0 * x))))
        
        # Additional coupling terms for improved discrimination
        f8 = 0.08 * np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8