import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial periodic component with modified frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f1 = 0.6 * (1.0 + np.sin(4.0 * r) * np.cos(3.0 * r) * np.sin(6.0 * r))
        
        # Asymmetric polynomial coupling with higher-order terms and modified exponents
        f2 = 0.4 * np.sum((x**4 + 0.6 * x**5 + 0.15 * x**6) * np.abs(x) ** 0.7)
        
        # Dynamic noise modulation with enhanced frequency components
        noise = np.sin(0.15 * np.sum(x**2)) * np.cos(0.08 * np.sum(x))
        f3 = 0.25 * np.sum(np.exp(-0.12 * np.abs(x)) * np.sin(12.0 * x) * noise)
        
        # Multi-scale interaction with adjusted log-scaled distances and enhanced sine modulation
        f4 = 0.2 * np.sum(np.sin(np.log(np.abs(x) + 1.5)) * np.cos(np.log(np.abs(x) + 1.5)))
        
        # Saddle point distribution with modified hyperbolic and polynomial components
        f5 = 0.3 * np.sum(np.tanh(x) * (x**3 - 1.0) * np.cos(4.0 * x))
        
        # Fractal-like structure with modified recursive polynomial transformations
        f6 = 0.15 * np.sum((x**3 + 0.12 * x**4) * np.sin(5.0 * x) * np.cos(4.0 * x))
        
        # Cross-term coupling with enhanced exponential decay and sinusoidal perturbations
        f7 = 0.15 * np.sum(np.exp(-0.6 * np.abs(x)) * np.sin(9.0 * x) * np.cos(7.0 * x))
        
        # Additional Gaussian-based interaction term for increased multimodality
        gaussian_term = np.sum(np.exp(-0.5 * ((x - 1.0)**2 + (x + 1.0)**2)))
        f8 = 0.1 * gaussian_term
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8