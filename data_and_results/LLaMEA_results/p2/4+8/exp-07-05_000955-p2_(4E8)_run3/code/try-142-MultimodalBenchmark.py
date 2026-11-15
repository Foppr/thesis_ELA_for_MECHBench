import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial periodic component with enhanced frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f1 = 0.8 * (1.0 + np.sin(3.0 * r) * np.cos(2.0 * r) * np.sin(5.0 * r))
        
        # Enhanced asymmetric polynomial coupling with higher exponents and weights
        f2 = 0.5 * np.sum((x**3.0 + 0.7 * x**4.0 + 0.2 * x**5.0) * np.abs(x) ** 0.7)
        
        # Amplified dynamic noise modulation with chaotic parameters
        noise = np.sin(0.15 * np.sum(x**2)) * np.cos(0.08 * np.sum(x))
        f3 = 0.3 * np.sum(np.exp(-0.15 * np.abs(x)) * np.sin(10.0 * x) * noise)
        
        # Multi-scale interaction with enhanced logarithmic scaling
        f4 = 0.2 * np.sum(np.sin(np.log(np.abs(x) + 1.5)) * np.cos(np.log(np.abs(x) + 1.5)))
        
        # Saddle point distribution with stronger hyperbolic and polynomial components
        f5 = 0.35 * np.sum(np.tanh(x) * (x**3 - 1.5) * np.cos(3.0 * x))
        
        # Fractal-like structure with recursive polynomial transformations and chaotic scaling
        f6 = 0.15 * np.sum((x**3.0 + 0.15 * x**4.0) * np.sin(4.0 * x) * np.cos(3.0 * x))
        
        # Cross-term coupling with exponential decay and sinusoidal perturbations
        f7 = 0.15 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(8.0 * x) * np.cos(6.0 * x))
        
        # Novel chaotic logistic map-based interaction term
        logistic_map = np.sum(4.0 * x * (1.0 - x))
        f8 = 0.2 * logistic_map
        
        # Additional high-frequency oscillation component
        f9 = 0.1 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9