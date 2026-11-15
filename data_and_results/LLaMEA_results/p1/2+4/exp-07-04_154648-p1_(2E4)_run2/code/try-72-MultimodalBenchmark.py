import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.tent_map_params = np.random.uniform(1.5, 2.0, dim)
        self.attraction_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.frequency_bases = np.random.uniform(1.0, 5.0, dim)
        self.spectral_weights = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic tent map component for dynamic landscape modulation
        tent_term = 0.0
        for i in range(self.dim):
            tent_map = self.tent_map_params[i] * np.abs(x_norm[i] - 0.5)
            tent_term += tent_map * np.sin(self.frequency_bases[i] * x_norm[i])
        
        # Gradient-based attraction fields with position-dependent strengths
        attraction_term = 0.0
        for i in range(10):
            diff = x_norm - self.attraction_centers[i]
            distance = np.sqrt(np.sum(diff**2))
            strength = 1.0 / (1.0 + distance**2)
            attraction_term += strength * np.sin(distance * 2 * np.pi)
        
        # Spectral decomposition using sine and cosine components
        spectral_term = 0.0
        for i in range(self.dim):
            spectral_term += (self.spectral_weights[i] * 
                             np.sin(self.frequency_bases[i] * x_norm[i]) * 
                             np.cos(self.frequency_bases[i] * x_norm[i]))
        
        # Cross-dimensional coupling with dynamic phase shifts
        coupling_term = 0.0
        for i in range(self.dim - 1):
            phase_shift = np.sin(x_norm[i] * x_norm[i+1])
            coupling_term += (x_norm[i]**2 + x_norm[i+1]**2) * phase_shift
        
        # Polynomial and interaction terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**4)
        interaction_term = 0.03 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Combine all components with global minimum at origin
        return tent_term + attraction_term + spectral_term + coupling_term + poly_term + interaction_term