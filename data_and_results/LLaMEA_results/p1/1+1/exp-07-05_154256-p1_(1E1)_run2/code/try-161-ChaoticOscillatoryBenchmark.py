import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 3.9  # Slightly increased chaos parameter for more erratic behavior
        self.freq = 7.0 * np.pi  # Increased frequency for more oscillations
        self.scale = 25.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance with modified log
            chaotic_factor = 1.0 + 0.8 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8))
        
        # Trigonometric oscillation component with modified frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) + np.sin(self.freq * x[i] * 0.7) * np.cos(self.freq * x[i] * 0.5)
        
        # Enhanced logistic map inspired interaction terms with quadratic coupling and cubic terms
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) + 0.12 * x[i]**3 * x[i+1]
        
        # Multi-scale oscillation with varying frequencies and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(18 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.13 * x[i]**4 + 0.07 * np.sin(25 * x[i])
        
        # Radial symmetry with polynomial decay and additional cosine term
        radial_symmetry = np.exp(-0.35 * r**2) * np.cos(self.freq * r) + 0.07 * r**3 + 0.04 * np.sin(12 * r)
        
        # Additional polynomial radial term for increased curvature
        poly_radial = 0.13 * r**4 + 0.07 * r**5
        
        # Add a new chaotic cross-term interaction between all dimensions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(self.r * x[i] * x[j]) * np.cos(self.r * x[i] * x[j] * 0.5)
        
        # Combine all components with adjusted weights
        return (0.36 * r**2 + 
                3.2 * trig_component + 
                0.58 * logistic_interaction + 
                1.15 * multi_scale + 
                0.32 * radial_symmetry + 
                0.22 * poly_radial + 
                0.32 * cross_term) * chaotic_factor