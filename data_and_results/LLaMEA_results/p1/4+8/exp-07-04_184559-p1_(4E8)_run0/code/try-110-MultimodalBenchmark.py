import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple exponential decays and cosine modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-3 * r**2) * np.cos(5 * np.pi * r) * np.sin(2 * np.pi * r))
        
        # Coupled spiral terms in multiple dimensions for rotational complexity
        spiral = 0.0
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(6 * theta) * np.cos(5 * theta) + 0.5 * np.sin(12 * theta)
            
        # Adaptive frequency modulation based on dimensionality
        freq_mod = 1.0 + 0.3 * np.sin(np.pi * self.dim / 4.0)
        oscillation = np.sum(np.sin(freq_mod * 8 * x_norm) * np.cos(freq_mod * 6 * x_norm))
        
        # Additional quadratic and quartic penalty terms for better conditioning
        penalty = 0.3 * np.sum(x_norm**2) + 0.1 * np.sum(x_norm**4)
        
        # Cross-term interaction for increased complexity
        if self.dim >= 2:
            cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:])))
        else:
            cross_term = 0.0
            
        # Chaotic perturbation component using logistic map for enhanced complexity
        chaotic = 0.0
        if self.dim >= 3:
            logistic_map = np.zeros(self.dim)
            r_param = 3.95
            for i in range(self.dim):
                if i == 0:
                    logistic_map[i] = 0.5
                else:
                    logistic_map[i] = r_param * logistic_map[i-1] * (1 - logistic_map[i-1])
            chaotic = np.sum(logistic_map * x_norm * np.cos(7 * x_norm))
        
        # Novel hybrid interaction term with sinusoidal coupling
        hybrid = 0.0
        if self.dim >= 4:
            for i in range(self.dim - 3):
                hybrid += np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[i+1]) * np.sin(2 * x_norm[i+2]) * np.cos(x_norm[i+3])
        
        # Combine all components with adjusted weights
        return radial + 1.5 * spiral + 0.8 * oscillation + penalty + 0.2 * cross_term + 0.3 * chaotic + 0.1 * hybrid