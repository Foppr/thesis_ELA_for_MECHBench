import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial periodic component with adaptive frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f1 = 0.6 * (1.0 + np.sin(3.1 * r) * np.cos(1.7 * r) * np.sin(4.2 * r))
        
        # Enhanced polynomial coupling with higher-order terms and altered exponents
        f2 = 0.4 * np.sum((x**2.7 + 0.7 * x**4.1 + 0.3 * x**5.2) * np.abs(x) ** 0.7)
        
        # Adaptive noise modulation with chaotic tent map
        noise = np.sin(0.21 * np.sum(x**2)) * np.cos(0.09 * np.sum(x))
        f3 = 0.25 * np.sum(np.exp(-0.21 * np.abs(x)) * np.sin(9.1 * x) * noise)
        
        # Multi-scale interaction with chaotic tent map scaling
        f4 = 0.18 * np.sum(np.sin(np.log(np.abs(x) + 1.7)) * np.cos(np.log(np.abs(x) + 1.7)))
        
        # Saddle point distribution with enhanced hyperbolic and polynomial components
        f5 = 0.3 * np.sum(np.tanh(x) * (x**2 - 1.3) * np.cos(2.7 * x))
        
        # Fractal-like structure with recursive polynomial transformations using tent map
        f6 = 0.12 * np.sum((x**3.1 + 0.21 * x**4.3) * np.sin(3.7 * x) * np.cos(2.7 * x))
        
        # Cross-term coupling with exponential decay and sinusoidal perturbations
        f7 = 0.12 * np.sum(np.exp(-0.55 * np.abs(x)) * np.sin(7.8 * x) * np.cos(5.8 * x))
        
        # Novel chaotic tent map-based interaction term
        tent_map = np.where(x >= 0, 2 * x, 2 * (1 - x))
        gaussian_term = np.sum(np.exp(-0.5 * (x**2 + 0.3 * x**4)) * tent_map)
        f8 = 0.15 * gaussian_term
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8