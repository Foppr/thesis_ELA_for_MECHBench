import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 4.1  # Increased chaos parameter for more erratic behavior
        self.freq = 9.0 * np.pi  # Increased frequency for more oscillations
        self.scale = 30.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance with modified log
            chaotic_factor = 1.0 + 0.9 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8))
        
        # Trigonometric oscillation component with modified frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) + np.sin(self.freq * x[i] * 0.7) * np.cos(self.freq * x[i] * 0.5)
        
        # Enhanced logistic map inspired interaction terms with quadratic coupling and cubic terms
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) + 0.15 * x[i]**3 * x[i+1]
        
        # Multi-scale oscillation with varying frequencies and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(20 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.25 * x[i]**2) + 0.15 * x[i]**4 + 0.08 * np.sin(30 * x[i])
        
        # Radial symmetry with polynomial decay and additional cosine term
        radial_symmetry = np.exp(-0.4 * r**2) * np.cos(self.freq * r) + 0.08 * r**3 + 0.05 * np.sin(15 * r)
        
        # Additional polynomial radial term for increased curvature
        poly_radial = 0.15 * r**4 + 0.08 * r**5
        
        # Add a new chaotic cross-term interaction between all dimensions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(self.r * x[i] * x[j]) * np.cos(self.r * x[i] * x[j] * 0.5)
        
        # Combine all components with adjusted weights
        return (0.4 * r**2 + 
                3.5 * trig_component + 
                0.62 * logistic_interaction + 
                1.2 * multi_scale + 
                0.35 * radial_symmetry + 
                0.25 * poly_radial + 
                0.35 * cross_term) * chaotic_factor