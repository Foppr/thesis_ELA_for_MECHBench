import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Radial polynomial decay term with chaotic tent map influence
        r = np.sqrt(np.sum(x_norm**2))
        tent_map = np.where(r < 0.5, 2 * r, 2 * (1 - r))
        radial_term = r**4 * np.exp(-r**2) * tent_map
        
        # Angular sine modulation with multiple frequencies
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sum([np.sin((i+1) * angles) * np.cos((i+1) * angles) 
                                 for i in range(min(3, self.dim))])
        else:
            angular_term = 0.0
            
        # Cross-term interactions with exponential decay
        cross_term = np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(3.0 * x_norm)**2)
        
        # Chaotic logistic map component for additional complexity
        logistic = 4.0 * r * (1 - r)
        logistic_term = logistic * np.exp(-0.1 * r**2)
        
        # Combine all terms with varying weights
        result = 0.4 * radial_term + 0.3 * angular_term + 0.2 * cross_term + 0.1 * logistic_term
        
        return result