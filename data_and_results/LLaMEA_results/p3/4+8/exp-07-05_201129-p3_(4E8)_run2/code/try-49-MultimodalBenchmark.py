import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Radial polynomial decay term with enhanced chaotic tent map influence
        r = np.sqrt(np.sum(x_norm**2))
        tent_map = np.where(r < 0.5, 2 * r, 2 * (1 - r))
        radial_term = r**5 * np.exp(-r**2) * tent_map
        
        # Angular sine modulation with increased frequencies
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sum([np.sin((i+1) * 2 * angles) * np.cos((i+1) * 2 * angles) 
                                 for i in range(min(4, self.dim))])
        else:
            angular_term = 0.0
            
        # Cross-term interactions with modified exponential decay and additional sine modulation
        cross_term = np.sum(np.exp(-0.3 * np.abs(x_norm)) * (np.sin(4.0 * x_norm)**2 + 0.5 * np.sin(2.0 * x_norm)**2))
        
        # Chaotic logistic map component with altered scaling
        logistic = 4.0 * r * (1 - r)
        logistic_term = logistic * np.exp(-0.15 * r**2)
        
        # Combine all terms with adjusted weights
        result = 0.35 * radial_term + 0.3 * angular_term + 0.25 * cross_term + 0.1 * logistic_term
        
        return result