import numpy as np

class MultiModalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced complexity
        self.freq_mod = 1.0 + 2.0 * np.random.rand()
        self.radial_scale = 0.5 + 1.5 * np.random.rand()
        self.conditioning_factor = 0.1 + 0.9 * np.random.rand()
        self.oscillation_amplitude = 0.5 + 2.0 * np.random.rand()
        self.interaction_strength = 0.3 + 1.2 * np.random.rand()
        self.terrain_roughness = 0.4 + 0.8 * np.random.rand()
        # Chaos parameters
        self.chaos_factor = 0.7 + 0.3 * np.random.rand()
        self.phase_shift = np.pi * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            sin_term += np.sin(freq * x[i] + self.phase_shift) * np.cos(0.3 * x[i])
        
        # Radial basis function component
        rb_term = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.5)
            width = 0.5 + 0.5 * np.cos(i * 0.3)
            rb_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Adaptive conditioning component
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + self.conditioning_factor * np.sin(0.4 * x[i])
            cond_term += (x[i]**2) * cond_factor
        
        # Chaotic interaction term
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                distance = np.abs(x[i] - x[j])
                interaction = self.interaction_strength * np.sin(self.chaos_factor * distance)
                chaos_term += interaction
        
        # Multi-scale terrain component
        terrain_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + self.terrain_roughness * np.sin(0.7 * x[i])
            terrain_term += scale * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i])
        
        # Combine all components with appropriate weights
        result = (self.oscillation_amplitude * sin_term + 
                 self.radial_scale * rb_term + 
                 self.conditioning_factor * cond_term + 
                 self.interaction_strength * chaos_term + 
                 self.terrain_roughness * terrain_term)
        
        return result