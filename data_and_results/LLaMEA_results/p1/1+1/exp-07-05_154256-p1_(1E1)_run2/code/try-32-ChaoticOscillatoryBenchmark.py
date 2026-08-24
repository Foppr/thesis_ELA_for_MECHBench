import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly altered chaotic behavior parameters
        self.r = 3.9  # Increased chaos parameter
        self.freq = 3.5 * np.pi  # Slightly increased frequency
        self.scale = 11.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance with modified log
            chaotic_factor = 1.0 + 0.5 * np.sin(self.r * np.log(r + 1e-8))
        
        # Trigonometric oscillation component with modified frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.4)
        
        # Enhanced logistic map inspired interaction terms with cubic coupling
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]**2) * (self.r * x[i] * (1 - x[i]**2))
        
        # Multi-scale oscillation with varying frequencies and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(16 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.12 * x[i]**2) + 0.12 * x[i]**5
        
        # Radial symmetry with polynomial decay and additional cosine term
        radial_symmetry = np.exp(-0.25 * r**2) * np.cos(self.freq * r) + 0.06 * r**4
        
        # Additional polynomial radial term for increased curvature
        poly_radial = 0.12 * r**5
        
        # Combine all components with adjusted weights
        return (0.35 * r**2 + 
                2.7 * trig_component + 
                0.5 * logistic_interaction + 
                0.85 * multi_scale + 
                0.35 * radial_symmetry + 
                0.18 * poly_radial) * chaotic_factor