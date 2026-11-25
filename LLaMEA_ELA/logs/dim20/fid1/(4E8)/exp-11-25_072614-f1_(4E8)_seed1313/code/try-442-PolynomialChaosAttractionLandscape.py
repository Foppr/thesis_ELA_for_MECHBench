import numpy as np

class PolynomialChaosAttractionLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters
        self.poly_degree = 3 + np.random.randint(0, 3)
        self.attraction_strength = 0.5 + 1.5 * np.random.rand()
        self.conditioning_scale = 0.1 + 0.9 * np.random.rand()
        self.spectral_density = 0.3 + 1.2 * np.random.rand()
        self.interaction_range = 0.8 + 1.2 * np.random.rand()
        # Chaos and spectral components
        self.chaos_magnitude = 0.4 + 0.6 * np.random.rand()
        self.phase_random = np.random.rand(self.dim) * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**self.poly_degree) * np.sin(self.phase_random[i])
            
        # Gradient-based attraction field
        attraction_term = 0.0
        for i in range(self.dim):
            attraction = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    influence = self.attraction_strength * np.exp(-distance / (self.interaction_range + 0.1))
                    attraction += influence * np.sin(0.5 * x[j])
            attraction_term += attraction
        
        # Spectral decomposition component
        spectral_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + self.spectral_density * np.cos(i * 0.3)
            spectral_term += np.sin(freq * x[i] + self.phase_random[i]) * np.cos(0.3 * x[i])
            
        # Adaptive conditioning based on distance from center
        cond_term = 0.0
        center = np.zeros(self.dim)
        for i in range(self.dim):
            cond_factor = 1.0 + self.conditioning_scale * np.sin(x[i] / 2.0)
            cond_term += (x[i]**2) * cond_factor
            
        # Chaos-induced perturbation
        chaos_term = 0.0
        for i in range(self.dim):
            chaos = self.chaos_magnitude * np.sin(3.0 * x[i] + 1.5 * np.cos(x[i]))
            chaos_term += chaos
            
        # Combine all components
        result = (poly_term + 
                 attraction_term + 
                 spectral_term + 
                 cond_term + 
                 chaos_term)
        
        return result