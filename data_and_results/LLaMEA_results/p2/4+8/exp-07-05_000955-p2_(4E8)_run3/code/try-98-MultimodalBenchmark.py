import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2) / self.dim
        
        # Nested chaotic maps with logistic and tent mappings
        f2 = 0.6 * np.sum(np.sin(20.0 * np.sin(15.0 * x)) * np.cos(12.0 * np.cos(10.0 * x)))
        
        # Quantum-inspired interference patterns using complex exponential terms
        f3 = 0.4 * np.sum(np.sin(3.0 * x) * np.cos(3.0 * x) * np.exp(-0.5 * x**2))
        
        # Memory-dependent fitness with delayed feedback and dynamic scaling
        f4 = 0.3 * np.sum(np.sin(5.0 * x) * np.cos(5.0 * x) * np.sin(0.1 * np.sum(x**2)))
        
        # Multi-scale fractal terrain with fractional Brownian motion inspired components
        f5 = 0.25 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.log(1.0 + np.abs(x)) * np.exp(-0.1 * np.abs(x)))
        
        # Saddle point generator with hyperbolic tangent and polynomial coupling
        f6 = 0.2 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.sin(7.0 * x))
        
        # Nested chaotic modulation with recursive trigonometric components
        f7 = 0.15 * np.sum(np.sin(np.sin(np.sin(4.0 * x))) * np.cos(np.cos(np.cos(3.0 * x))))
        
        # Quantum tunneling effect with probabilistic weighting
        f8 = 0.1 * np.sum(np.sin(2.0 * x) * np.cos(2.0 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Memory-based adaptive modulation with time-dependent coefficients
        f9 = 0.1 * np.sum(np.sin(10.0 * x) * np.cos(10.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9