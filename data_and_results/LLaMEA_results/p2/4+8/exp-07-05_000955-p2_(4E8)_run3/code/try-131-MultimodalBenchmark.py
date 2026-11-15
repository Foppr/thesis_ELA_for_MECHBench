import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial periodic component with higher frequency harmonics
        r = np.sqrt(np.sum(x**2))
        f1 = 0.6 * (1.0 + np.sin(4.0 * r) * np.cos(3.0 * r) * np.sin(6.0 * r) * np.cos(2.0 * r))
        
        # Asymmetric polynomial coupling with modified exponents and cross-terms
        f2 = 0.25 * np.sum((x**3 + 0.3 * x**4 + 0.05 * x**5) * np.abs(x) ** 0.7)
        
        # Improved dynamic noise modulation with adaptive frequency
        noise = np.sin(0.15 * np.sum(x**2)) * np.cos(0.08 * np.sum(x))
        f3 = 0.22 * np.sum(np.exp(-0.12 * np.abs(x)) * np.sin(12.0 * x) * noise)
        
        # Multi-scale interaction with enhanced logarithmic scaling
        f4 = 0.18 * np.sum(np.sin(np.log(np.abs(x) + 1.5)) * np.cos(np.log(np.abs(x) + 1.5)))
        
        # Enhanced saddle point distribution with hyperbolic and polynomial components
        f5 = 0.28 * np.sum(np.tanh(x) * (x**2 - 1.2) * np.cos(3.5 * x))
        
        # Fractal-like structure with modified recursive polynomial transformations
        f6 = 0.12 * np.sum((x**2 + 0.15 * x**3) * np.sin(5.0 * x) * np.cos(4.0 * x))
        
        # Cross-term coupling with exponential decay and sinusoidal perturbations
        f7 = 0.15 * np.sum(np.exp(-0.6 * np.abs(x)) * np.sin(9.0 * x) * np.cos(7.0 * x))
        
        # Additional interaction term for increased complexity and better separation of optima
        f8 = 0.08 * np.sum(np.sin(2.0 * x) * np.cos(2.0 * x) * np.exp(-0.2 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8