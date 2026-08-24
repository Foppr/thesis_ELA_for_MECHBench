import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial periodic component with enhanced frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f1 = 0.8 * (1.0 + np.sin(4.2 * r) * np.cos(2.1 * r) * np.sin(5.3 * r) * np.cos(3.7 * r))
        
        # Complex polynomial coupling with higher exponents and stronger weights
        f2 = 0.5 * np.sum((x**3.2 + 0.7 * x**4.1 + 0.3 * x**5.2 + 0.1 * x**6.8) * np.abs(x) ** 0.7)
        
        # Enhanced noise modulation with chaotic logistic map
        noise = np.sin(0.23 * np.sum(x**2)) * np.cos(0.12 * np.sum(x))
        logistic_noise = 1.0 - 1.5 * np.prod(np.sin(0.3 * x) + 0.5)
        f3 = 0.3 * np.sum(np.exp(-0.23 * np.abs(x)) * np.sin(10.1 * x) * noise * logistic_noise)
        
        # Multi-scale interaction with fractal-like logarithmic scaling
        f4 = 0.22 * np.sum(np.sin(np.log(np.abs(x) + 2.1)) * np.cos(np.log(np.abs(x) + 2.1)) * np.sin(2.3 * x))
        
        # Enhanced saddle point distribution with hyperbolic and polynomial components
        f5 = 0.35 * np.sum(np.tanh(x) * (x**3 - 1.5) * np.cos(3.2 * x) * np.sin(1.8 * x))
        
        # Fractal-like structure with recursive polynomial transformations and chaotic perturbations
        f6 = 0.15 * np.sum((x**3.7 + 0.23 * x**4.8) * np.sin(4.2 * x) * np.cos(3.1 * x) * np.tan(0.5 * x))
        
        # Cross-term coupling with exponential decay, sinusoidal perturbations, and chaotic modulation
        f7 = 0.18 * np.sum(np.exp(-0.67 * np.abs(x)) * np.sin(9.3 * x) * np.cos(6.8 * x) * np.sin(0.4 * np.sum(x**2)))
        
        # Novel Gaussian-based interaction term with chaotic modulation
        gaussian_term = np.sum(np.exp(-0.5 * (x**2 + 0.35 * x**4 + 0.12 * x**6)))
        f8 = 0.2 * gaussian_term
        
        # Add a chaotic logistic map component for additional complexity
        logistic_component = np.sum(4.0 * x * (1.0 - x))
        f9 = 0.1 * logistic_component
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9