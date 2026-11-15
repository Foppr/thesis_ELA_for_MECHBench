import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial periodic component with modified frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f1 = 0.6 * (1.0 + np.sin(2.5 * r) * np.cos(1.5 * r) * np.sin(4.0 * r))
        
        # Asymmetric polynomial coupling with altered exponents and weights
        f2 = 0.4 * np.sum((x**2.5 + 0.6 * x**3.5 + 0.15 * x**4.5) * np.abs(x) ** 0.6)
        
        # Dynamic noise modulation with adjusted parameters
        noise = np.sin(0.12 * np.sum(x**2)) * np.cos(0.06 * np.sum(x))
        f3 = 0.25 * np.sum(np.exp(-0.12 * np.abs(x)) * np.sin(9.0 * x) * noise)
        
        # Multi-scale interaction with modified logarithmic scaling
        f4 = 0.18 * np.sum(np.sin(np.log(np.abs(x) + 1.2)) * np.cos(np.log(np.abs(x) + 1.2)))
        
        # Saddle point distribution with enhanced hyperbolic and polynomial components
        f5 = 0.3 * np.sum(np.tanh(x) * (x**2 - 1.2) * np.cos(2.5 * x))
        
        # Fractal-like structure with modified recursive polynomial transformations
        f6 = 0.12 * np.sum((x**2.5 + 0.12 * x**3.5) * np.sin(3.5 * x) * np.cos(2.5 * x))
        
        # Cross-term coupling with exponential decay and sinusoidal perturbations
        f7 = 0.12 * np.sum(np.exp(-0.45 * np.abs(x)) * np.sin(7.5 * x) * np.cos(5.5 * x))
        
        # Novel Gaussian-based interaction term
        gaussian_term = np.sum(np.exp(-0.5 * (x**2 + 0.2 * x**4)))
        f8 = 0.15 * gaussian_term
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8