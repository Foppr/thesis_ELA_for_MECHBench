import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        # Initialize logistic map parameters for chaos generation
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.logistic_states = np.random.rand(dim) * 0.1 + 0.1
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal multimodal component using logistic map chaos
        fractal_term = 0.0
        for i in range(self.dim):
            # Update logistic map state
            self.logistic_states[i] = self.r_values[i] * self.logistic_states[i] * (1 - self.logistic_states[i])
            # Use chaotic state to modulate multimodal function
            chaos_mod = 0.5 + 0.5 * np.sin(3.0 * self.t + 2.0 * self.logistic_states[i])
            fractal_term += chaos_mod * (x[i]**2 - 10 * np.cos(0.5 * x[i]) + 20)
        
        # Gradient-guided basin hopping with periodic forcing
        basin_hopping = 0.0
        for i in range(self.dim):
            # Periodic forcing term to guide search
            forcing = np.sin(0.3 * self.t + i * 0.7) * np.cos(0.2 * self.t + i * 0.4)
            # Basin center influenced by chaotic dynamics
            center = 2.0 * np.sin(0.5 * self.t + i * 0.3) + 0.5 * self.logistic_states[i]
            basin_hopping += (x[i] - center)**2 * (1.0 + 0.1 * forcing)
        
        # Self-similar structure using fractional Brownian motion scaling
        fbm_term = 0.0
        for i in range(self.dim):
            # Scale based on dimension and time
            scale = 1.0 + 0.2 * np.sin(0.4 * self.t + i * 0.5)
            # Create self-similar pattern with multiple frequencies
            freqs = [1.0, 2.0, 3.0]
            for f in freqs:
                fbm_term += scale * np.sin(f * x[i] + self.t) * (1.0 / (f**1.5))
        
        # Dynamic penalty based on distance from fractal centers
        penalty = 0.0
        for i in range(self.dim):
            # Multiple fractal centers at different scales
            center_dist = np.abs(x[i] - 2.0 * np.sin(0.3 * self.t + i * 0.5))
            if center_dist < 1.0:
                penalty += 5.0 * (1.0 - center_dist)**2
        
        # Combine all components with time-varying weights
        w1 = 0.3 + 0.1 * np.sin(0.5 * self.t)
        w2 = 0.4 + 0.15 * np.cos(0.6 * self.t)
        w3 = 0.2 + 0.05 * np.sin(0.7 * self.t)
        w4 = 0.1 + 0.05 * np.cos(0.8 * self.t)
        
        result = w1 * fractal_term + w2 * basin_hopping + w3 * fbm_term + w4 * penalty
        
        # Apply dimensionality scaling
        if self.dim > 1:
            scale_factor = 1.0 + 0.05 * np.log(self.dim) + 0.005 * self.dim**1.2
            result *= scale_factor
            
        return result