import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial = r * (1.0 + 0.3 * np.sin(3.0 * r))
        
        # Trigonometric interactions between dimensions
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_interaction += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Adaptive conditioning based on distance from origin
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1.0 + 0.5 * np.sin(r)) * x[i]**4
        
        # Multimodal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(5.0 * x[i]) * np.cos(2.0 * x[i]) + 0.1 * x[i]**2
        
        # Cross-term interactions with exponential decay
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(2.0 * x[i] * x[j])
        
        # Global scaling and offset
        scale = 1.0 + 0.2 * np.sin(0.5 * r)
        
        return scale * (radial + 0.5 * trig_interaction + 0.3 * conditioning + 0.4 * multimodal + 0.2 * cross_terms)