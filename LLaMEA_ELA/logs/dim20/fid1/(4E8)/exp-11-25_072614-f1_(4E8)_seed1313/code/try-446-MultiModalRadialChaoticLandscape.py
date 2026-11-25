import numpy as np

class MultiModalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.freq_mod = 2.0 + 3.0 * np.random.rand()
        self.radial_scale = 1.0 + 2.0 * np.random.rand()
        self.conditioning_factor = 0.2 + 1.5 * np.random.rand()
        self.oscillation_amplitude = 1.0 + 3.0 * np.random.rand()
        self.interaction_strength = 0.5 + 2.0 * np.random.rand()
        self.terrain_roughness = 0.8 + 1.2 * np.random.rand()
        # Advanced chaos parameters
        self.chaos_factor = 1.0 + 0.5 * np.random.rand()
        self.phase_shift = np.pi * np.random.rand()
        # Enhanced chaotic coupling parameter
        self.coupling_strength = 0.5 + 1.5 * np.random.rand()
        # Additional dynamic parameters
        self.nested_factor = 0.3 + 1.0 * np.random.rand()
        self.multiscale_depth = 1.5 + 2.5 * np.random.rand()
        self.adaptive_damping = 0.1 + 0.9 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with nested frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.freq_mod * (1.0 + 0.3 * np.sin(i * 0.5))
            sin_term += np.sin(freq * x[i] + self.phase_shift) * np.cos(0.4 * x[i]) * np.exp(-self.nested_factor * x[i]**2)
        
        # Enhanced radial basis function component with dynamic centers
        rb_term = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.7) + 1.5 * np.cos(i * 0.3)
            width = 0.3 + 0.7 * np.cos(i * 0.4)
            rb_term += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1.0 + self.multiscale_depth * np.sin(0.6 * x[i]))
        
        # Enhanced adaptive conditioning component
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + self.conditioning_factor * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            cond_term += (x[i]**2) * cond_factor * (1.0 + self.adaptive_damping * np.tanh(x[i]))
        
        # Enhanced chaotic interaction term with dynamic coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                distance = np.abs(x[i] - x[j])
                # Dynamic chaotic interaction with multiple nonlinear couplings
                interaction = self.interaction_strength * np.sin(self.chaos_factor * distance) * np.cos(self.coupling_strength * (x[i] + x[j])) * np.tanh(0.5 * (x[i] - x[j]))
                chaos_term += interaction
        
        # Enhanced multi-scale terrain component
        terrain_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + self.terrain_roughness * np.sin(0.8 * x[i]) * np.cos(0.4 * x[i])
            terrain_term += scale * np.cos(0.6 * x[i]) * np.sin(0.4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Additional nested valley component
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Combine all components with appropriate weights
        result = (self.oscillation_amplitude * sin_term + 
                 self.radial_scale * rb_term + 
                 self.conditioning_factor * cond_term + 
                 self.interaction_strength * chaos_term + 
                 self.terrain_roughness * terrain_term + 
                 0.5 * valley_term)
        
        return result