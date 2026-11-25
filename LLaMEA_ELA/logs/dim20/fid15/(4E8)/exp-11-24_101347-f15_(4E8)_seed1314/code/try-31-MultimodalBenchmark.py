import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.1 * r) * np.sin(3.0 * r)
        
        # Trigonometric coupling between dimensions
        trig_coupling = np.prod(np.cos(2.0 * x) + 1.0)
        
        # Polynomial perturbation
        poly_perturb = 0.01 * np.sum(x**6)
        
        # Additional multimodal term
        multi_term = np.sum(np.sin(4.0 * x) * np.cos(6.0 * x))
        
        return radial + trig_coupling + poly_perturb + multi_term