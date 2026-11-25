import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with varying difficulty per dimension
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.3 * r**2 * np.exp(-0.1 * r)
        
        # Periodic forcing with dimensionally varying frequencies
        freqs = np.linspace(1.0, 5.0, self.dim)
        periodic_term = np.sum(np.sin(freqs * x) * np.cos(freqs * x))
        
        # Asymmetric gradient structure with cross-dimensional coupling
        grad_structure = 0.2 * np.sum(x * np.sin(3.0 * x) * np.exp(-0.5 * x**2))
        
        # Multi-scale harmonic interference with radial modulation
        scale_term = 0.25 * np.sum(np.sin(10.0 * x + np.cos(5.0 * x)) * np.cos(8.0 * x + np.sin(4.0 * x)))
        
        # Dimensional weighting to create varying difficulty across dimensions
        weights = np.linspace(0.5, 2.0, self.dim)
        weight_term = np.sum(weights * x**3.0 * np.exp(-0.3 * np.abs(x)))
        
        # Saddle point structure with radial symmetry and chaotic modulation
        saddle_term = 0.15 * np.sum(np.sin(7.0 * x) * np.cos(6.0 * x) * np.exp(-0.2 * r**2))
        
        # Combine all components
        return radial_term + periodic_term + grad_structure + scale_term + weight_term + saddle_term