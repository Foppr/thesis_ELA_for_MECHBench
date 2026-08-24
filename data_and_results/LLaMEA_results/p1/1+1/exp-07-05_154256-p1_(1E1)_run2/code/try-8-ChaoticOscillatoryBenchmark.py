import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 3.9  # Logistic map parameter for chaos
        self.freq = 2.0 * np.pi
        self.scale = 10.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance
            chaotic_factor = 1.0 + 0.5 * np.sin(self.r * np.log(r + 1e-10))
        
        # Trigonometric oscillation component
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.5)
        
        # Logistic map inspired interaction terms
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]))
        
        # Multi-scale oscillation with varying frequencies
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial symmetry with exponential decay
        radial_symmetry = np.exp(-0.5 * r**2) * np.cos(self.freq * r)
        
        # Combine all components with adaptive weights
        return (0.3 * r**2 + 
                2.0 * trig_component + 
                0.5 * logistic_interaction + 
                0.8 * multi_scale + 
                0.2 * radial_symmetry) * chaotic_factor