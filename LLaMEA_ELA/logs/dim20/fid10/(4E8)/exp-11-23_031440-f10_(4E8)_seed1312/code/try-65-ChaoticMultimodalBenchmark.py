import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component for non-linearity with enhanced sensitivity
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x_norm[-1]
            else:
                x_prev = x_norm[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(2 * np.pi * x_prev)
        
        # Exponential decay interactions between dimensions with added coupling
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_decay += np.exp(-dist) * np.sin(np.pi * dist) * np.cos(0.5 * np.pi * dist)
        
        # Dynamic conditioning based on radial position with increased complexity and nonlinearity
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 4.0 * np.sin(4 * np.pi * r)**3
        
        # Multi-modal sinusoidal terms with varying frequencies, added phase shifts, and cubic components
        modal_terms = 0.0
        for i in range(self.dim):
            freq = (i % 7) + 1
            phase = np.pi * (i / self.dim)
            modal_terms += (np.sin(freq * np.pi * x_norm[i] + phase) * 
                           np.cos(freq * np.pi * x_norm[i] + phase) + 
                           0.3 * x_norm[i]**3)
        
        # Add a quadratic basin term with variable weights to create deeper regions
        quadratic_basin = 0.15 * np.sum(x_norm**2) + 0.05 * np.sum(x_norm**4)
        
        # Combine all terms with modified weighting and added cross-terms
        result = condition_factor * (0.7 * r**2 + 0.2 * chaotic_term + 0.15 * exp_decay + 
                                   0.3 * modal_terms + quadratic_basin)
        
        return result