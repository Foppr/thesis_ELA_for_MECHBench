import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave component with fractional frequencies and phase modulation
        r = np.sqrt(np.sum(x**2))
        f1 = 0.6 * np.sin(7.0 * r) * np.cos(4.0 * r) * np.sin(9.0 * r) * np.exp(-0.1 * r)
        
        # Quantum-inspired polynomial coupling with complex exponents and phase shifts
        f2 = 0.4 * np.sum((x**3.5 + 0.3 * x**4.2 + 0.05 * x**5.1) * np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Adaptive fractal noise with dynamic scaling and chaotic modulation
        noise = np.sin(0.2 * np.sum(x**2)) * np.cos(0.1 * np.sum(x)) * np.exp(-0.05 * r)
        f3 = 0.3 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(15.0 * x) * noise * np.sin(3.0 * r))
        
        # Multi-scale chaotic interaction with log-scaled distances and hyperbolic modulation
        f4 = 0.2 * np.sum(np.tanh(np.log(np.abs(x) + 1.0)) * np.cos(np.log(np.abs(x) + 1.0)) * np.sin(2.0 * r))
        
        # Saddle point distribution with hyperbolic and polynomial components with chaotic perturbations
        f5 = 0.3 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.cos(5.0 * x) * np.sin(2.0 * r))
        
        # Fractal-like structure using recursive polynomial transformations with quantum-like interference
        f6 = 0.2 * np.sum((x**2.5 + 0.2 * x**3.3) * np.sin(6.0 * x) * np.cos(4.0 * x) * np.exp(-0.1 * r))
        
        # Cross-term coupling with exponential decay, sinusoidal perturbations, and chaotic modulation
        f7 = 0.25 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(12.0 * x) * np.cos(9.0 * x) * np.sin(4.0 * r))
        
        # Additional chaotic coupling term with fractional dimensions and complex phase interactions
        f8 = 0.15 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.sin(3.0 * r) * np.exp(-0.05 * r))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8