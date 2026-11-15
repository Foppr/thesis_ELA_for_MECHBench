import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial periodic component with multiple frequency harmonics
        r = np.sqrt(np.sum(x**2))
        f1 = 0.6 * (1.0 + np.sin(2.5 * r) * np.cos(3.0 * r) * np.sin(4.0 * r) * np.cos(1.5 * r))
        
        # Asymmetric polynomial coupling with modified exponents and cross-terms
        f2 = 0.25 * np.sum((x**3 + 0.3 * x**4 + 0.05 * x**5) * np.abs(x) ** 0.7)
        
        # Improved dynamic noise modulation with adaptive scaling
        noise = np.sin(0.15 * np.sum(x**2)) * np.cos(0.08 * np.sum(x))
        f3 = 0.15 * np.sum(np.exp(-0.15 * np.abs(x)) * np.sin(12.0 * x) * noise)
        
        # Multi-scale interaction with enhanced sine modulation and log-scaling
        f4 = 0.2 * np.sum(np.sin(np.log(np.abs(x) + 1.5)) * np.cos(np.log(np.abs(x) + 1.5)))
        
        # Enhanced saddle point distribution with hyperbolic and polynomial components
        f5 = 0.3 * np.sum(np.tanh(x) * (x**2 - 1.5) * np.cos(2.5 * x))
        
        # Fractal-like structure with modified recursive transformations
        f6 = 0.15 * np.sum((x**2 + 0.15 * x**3) * np.sin(3.5 * x) * np.cos(2.5 * x))
        
        # Cross-term coupling with modified exponential decay and sinusoidal perturbations
        f7 = 0.12 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(9.0 * x) * np.cos(5.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7