import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component for non-linearity
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x_norm[-1]
            else:
                x_prev = x_norm[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Exponential decay interactions between dimensions
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_decay += np.exp(-dist) * np.sin(np.pi * dist)
        
        # Dynamic conditioning based on radial position with increased complexity
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 3.0 * np.sin(3 * np.pi * r)**2
        
        # Multi-modal sinusoidal terms with varying frequencies and added quadratic component
        modal_terms = 0.0
        for i in range(self.dim):
            freq = (i % 5) + 1
            modal_terms += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Add a quadratic basin term to create deeper regions
        quadratic_basin = 0.1 * np.sum(x_norm**2)
        
        # Combine all terms with modified weighting
        result = condition_factor * (0.6 * r**2 + 0.3 * chaotic_term + 0.2 * exp_decay + 0.4 * modal_terms + quadratic_basin)
        
        return result