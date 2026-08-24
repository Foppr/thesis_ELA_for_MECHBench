import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for enhanced chaotic behavior
        self.r = 4.0  # Increased chaos parameter for more erratic dynamics
        self.freq = 4.0 * np.pi  # Higher frequency for denser oscillations
        self.scale = 15.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply enhanced chaotic scaling based on radial distance with double log
            chaotic_factor = 1.0 + 0.8 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8))
        
        # Trigonometric oscillation component with multiple frequency harmonics
        trig_component = 0
        for i in range(self.dim):
            trig_component += (np.sin(self.freq * x[i]) * 
                              np.cos(self.freq * x[i] * 0.3) * 
                              np.sin(self.freq * x[i] * 0.7) * 
                              np.cos(self.freq * x[i] * 1.2))
        
        # Enhanced logistic map inspired interaction terms with cubic coupling
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**3))
        
        # Multi-scale oscillation with varying frequencies and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += (np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.15 * x[i]**2) + 
                           0.1 * x[i]**4 + 
                           0.05 * np.sin(25 * x[i]) * np.cos(10 * x[i]))
        
        # Radial symmetry with polynomial decay and additional cosine term
        radial_symmetry = np.exp(-0.3 * r**2) * np.cos(self.freq * r) + 0.05 * r**3 + 0.02 * np.sin(5 * r)
        
        # Additional polynomial radial term for increased curvature
        poly_radial = 0.1 * r**4 + 0.05 * r**6
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i] * x[j]) * np.sin(self.r * (x[i] + x[j]))
        
        # Combine all components with adjusted weights
        return (0.4 * r**2 + 
                3.0 * trig_component + 
                0.8 * logistic_interaction + 
                1.2 * multi_scale + 
                0.4 * radial_symmetry + 
                0.2 * poly_radial + 
                0.3 * cross_coupling) * chaotic_factor