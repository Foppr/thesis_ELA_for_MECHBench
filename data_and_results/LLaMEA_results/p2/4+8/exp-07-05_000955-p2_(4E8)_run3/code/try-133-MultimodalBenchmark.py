import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial periodic component with higher frequency modulation
        r = np.sqrt(np.sum(x**2))
        f1 = 1.2 * (1.0 + np.sin(5.2 * r) * np.cos(3.1 * r) * np.sin(7.8 * r))
        
        # Enhanced asymmetric polynomial coupling with higher exponents and weights
        f2 = 0.8 * np.sum((x**3.5 + 0.7 * x**4.2 + 0.3 * x**5.1) * np.abs(x) ** 0.7)
        
        # Amplified dynamic noise modulation with chaotic sine-cosine interactions
        noise = np.sin(0.3 * np.sum(x**2)) * np.cos(0.1 * np.sum(x)) * np.sin(0.05 * np.sum(x**3))
        f3 = 0.4 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(12.0 * x) * noise)
        
        # Multi-scale interaction with enhanced logarithmic scaling and chaotic perturbations
        f4 = 0.3 * np.sum(np.sin(np.log(np.abs(x) + 2.0)) * np.cos(np.log(np.abs(x) + 2.0)) * np.sin(2.0 * np.log(np.abs(x) + 2.0)))
        
        # Enhanced saddle point distribution with hyperbolic and polynomial components
        f5 = 0.5 * np.sum(np.tanh(x) * (x**3 - 1.5) * np.cos(3.5 * x))
        
        # Fractal-like structure with recursive polynomial transformations and chaotic scaling
        f6 = 0.25 * np.sum((x**3.8 + 0.2 * x**4.5) * np.sin(4.5 * x) * np.cos(3.5 * x) * np.sin(0.5 * r))
        
        # Enhanced cross-term coupling with exponential decay and multi-frequency sinusoidal perturbations
        f7 = 0.2 * np.sum(np.exp(-0.7 * np.abs(x)) * np.sin(10.0 * x) * np.cos(8.0 * x) * np.sin(3.0 * x))
        
        # Novel chaotic logistic map-based interaction term
        logistic_map = np.sum(4 * x * (1 - x))
        f8 = 0.2 * logistic_map
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8