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
        radial_term = r**6 * np.exp(-r**3) * tent_map * np.sin(5 * r)
        
        # Angular sine modulation with multiple frequencies and phase shifts
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sum([np.sin((i+1) * angles + i * np.pi/4) * np.cos((i+1) * angles + i * np.pi/6) 
                                 for i in range(min(5, self.dim))])
        else:
            angular_term = 0.0
            
        # Cross-term interactions with enhanced exponential decay and trigonometric mixing
        cross_term = np.sum(np.exp(-0.3 * np.abs(x_norm)) * (np.sin(4.0 * x_norm)**2 + np.cos(2.0 * x_norm)**2))
        
        # Chaotic logistic map component with multiple feedback loops
        logistic = 4.0 * r * (1 - r)
        logistic_term = logistic**2 * np.exp(-0.2 * r**2) * np.sin(3 * r)
        
        # Additional high-frequency sinusoidal modulation for increased complexity
        high_freq_term = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        # Combine all terms with varying weights and add a conditioning factor
        result = 0.3 * radial_term + 0.25 * angular_term + 0.2 * cross_term + 0.15 * logistic_term + 0.1 * high_freq_term
        
        return result