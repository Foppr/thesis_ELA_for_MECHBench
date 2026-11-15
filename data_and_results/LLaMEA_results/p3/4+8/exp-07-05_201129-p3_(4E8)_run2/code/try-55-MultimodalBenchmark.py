import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Radial term with enhanced chaotic tent map and polynomial decay
        r = np.sqrt(np.sum(x_norm**2))
        tent_map = np.where(r < 0.5, 2 * r, 2 * (1 - r))
        radial_term = r**6 * np.exp(-r**3) * tent_map * (1 + 0.5 * np.sin(10 * r))
        
        # Multi-frequency angular sine modulation with varying amplitudes
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sum([np.sin((i+1)**2 * angles) * np.cos((i+1)**1.5 * angles) 
                                 for i in range(min(4, self.dim))])
            angular_term *= (1 + 0.3 * np.cos(5 * angles))
        else:
            angular_term = 0.0
            
        # Cross-term interactions with hyperbolic tangent and multiple decay factors
        cross_term = np.sum(np.tanh(2.0 * x_norm) * np.sin(5.0 * x_norm)**3)
        cross_term += np.sum(np.exp(-0.3 * np.abs(x_norm)) * np.cos(4.0 * x_norm)**2)
        
        # Novel chaotic logistic map with time-varying parameter
        logistic = 4.0 * r * (1 - r)
        logistic_term = logistic * np.exp(-0.2 * r**3) * (1 + 0.2 * np.sin(15 * r))
        
        # Additional harmonic component with asymmetric decay
        harmonic_term = np.sum(np.sin(2.0 * x_norm)**4 + np.cos(3.0 * x_norm)**4)
        harmonic_term *= np.exp(-0.1 * r**2)
        
        # Combine all terms with adaptive weights based on dimensionality
        weight_radial = 0.35 + 0.05 * np.sin(self.dim)
        weight_angular = 0.25 + 0.03 * np.cos(self.dim)
        weight_cross = 0.20 + 0.02 * np.sin(self.dim * 0.5)
        weight_logistic = 0.15 + 0.04 * np.cos(self.dim * 0.7)
        weight_harmonic = 0.05
        
        result = (weight_radial * radial_term + 
                 weight_angular * angular_term + 
                 weight_cross * cross_term + 
                 weight_logistic * logistic_term + 
                 weight_harmonic * harmonic_term)
        
        return result