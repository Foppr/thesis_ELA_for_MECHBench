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
        radial_term = r**5 + 0.3 * r**7 + 0.1 * r**9
        
        # Implicit surface interaction terms with stronger coupling
        surface_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupled interaction between dimensions
                interaction = np.sin(x_norm[i] * x_norm[j] * 2 * np.pi) * np.exp(-0.5 * r)
                surface_terms.append(interaction)
        
        # Multi-scale radial sinusoidal oscillation
        oscillation = np.sum(np.sin(7 * r * np.pi) + 0.5 * np.sin(14 * r * np.pi))
        
        # High-frequency multi-modal component with variable frequency
        modal_component = np.sum(np.sin(25 * x_norm**2) + 0.3 * np.sin(50 * x_norm**2))
        
        # Cross-term interactions for increased complexity
        cross_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross = np.cos(x_norm[i] * x_norm[j] * 3 * np.pi) * (x_norm[i]**2 + x_norm[j]**2)
                cross_terms.append(cross)
        
        # Combined fitness function with adjusted weights
        return radial_term + 0.15 * np.sum(surface_terms) + 0.08 * oscillation + 0.03 * modal_component + 0.05 * np.sum(cross_terms)