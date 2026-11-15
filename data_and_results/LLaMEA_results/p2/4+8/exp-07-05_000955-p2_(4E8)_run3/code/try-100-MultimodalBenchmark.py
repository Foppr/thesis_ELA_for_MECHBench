import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial periodic component with varying frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f1 = 0.5 * (1.0 + np.sin(3.0 * r) * np.cos(2.0 * r) * np.sin(5.0 * r))
        
        # Asymmetric polynomial coupling with mixed exponents
        f2 = 0.3 * np.sum((x**3 + 0.5 * x**4 + 0.1 * x**5) * np.abs(x) ** 0.5)
        
        # Dynamic noise modulation with time-like parameter
        noise = np.sin(0.1 * np.sum(x**2)) * np.cos(0.05 * np.sum(x))
        f3 = 0.2 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * noise)
        
        # Multi-scale interaction with log-scaled distances and sine modulation
        f4 = 0.15 * np.sum(np.sin(np.log(np.abs(x) + 1.0)) * np.cos(np.log(np.abs(x) + 1.0)))
        
        # Saddle point distribution with hyperbolic and polynomial components
        f5 = 0.25 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.cos(3.0 * x))
        
        # Fractal-like structure using recursive polynomial transformations
        f6 = 0.1 * np.sum((x**2 + 0.1 * x**3) * np.sin(4.0 * x) * np.cos(3.0 * x))
        
        # Cross-term coupling with exponential decay and sinusoidal perturbations
        f7 = 0.1 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(8.0 * x) * np.cos(6.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7