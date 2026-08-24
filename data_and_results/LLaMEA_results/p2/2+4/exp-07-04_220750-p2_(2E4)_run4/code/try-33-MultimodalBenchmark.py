import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Radial component with polynomial growth
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = r**4 + 0.5 * r**6
        
        # Implicit surface interaction terms
        surface_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupled interaction between dimensions
                interaction = np.sin(x_norm[i] * x_norm[j] * np.pi)
                surface_terms.append(interaction)
        
        # Radial sinusoidal oscillation
        oscillation = np.sum(np.sin(5 * r * np.pi))
        
        # High-frequency multi-modal component
        modal_component = np.sum(np.sin(20 * x_norm**2))
        
        # Combined fitness function
        return radial_term + 0.1 * np.sum(surface_terms) + 0.05 * oscillation + 0.02 * modal_component