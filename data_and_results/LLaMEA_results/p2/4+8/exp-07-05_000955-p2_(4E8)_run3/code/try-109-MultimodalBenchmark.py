import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial periodic component with modified frequencies
        r = np.sqrt(np.sum(x**2))
        f1 = 0.5 * (1.0 + np.sin(2.5 * r) * np.cos(1.5 * r) * np.sin(4.0 * r))
        
        # Asymmetric polynomial coupling with altered exponents
        f2 = 0.35 * np.sum((x**3 + 0.4 * x**4 + 0.15 * x**5) * np.abs(x) ** 0.6)
        
        # Dynamic noise modulation with updated parameters
        noise = np.sin(0.12 * np.sum(x**2)) * np.cos(0.06 * np.sum(x))
        f3 = 0.22 * np.sum(np.exp(-0.12 * np.abs(x)) * np.sin(9.0 * x) * noise)
        
        # Multi-scale interaction with modified sine modulation
        f4 = 0.16 * np.sum(np.sin(np.log(np.abs(x) + 1.2)) * np.cos(np.log(np.abs(x) + 1.2)))
        
        # Saddle point distribution with adjusted hyperbolic components
        f5 = 0.26 * np.sum(np.tanh(x) * (x**2 - 1.2) * np.cos(2.5 * x))
        
        # Fractal-like structure with modified transformations
        f6 = 0.11 * np.sum((x**2 + 0.12 * x**3) * np.sin(3.5 * x) * np.cos(2.5 * x))
        
        # Cross-term coupling with modified decay and perturbations
        f7 = 0.11 * np.sum(np.exp(-0.45 * np.abs(x)) * np.sin(7.5 * x) * np.cos(5.5 * x))
        
        # Novel Gaussian-based interaction term
        gaussian_term = np.sum(np.exp(-0.5 * (x**2 + 0.2 * x**4)))
        f8 = 0.15 * gaussian_term
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8