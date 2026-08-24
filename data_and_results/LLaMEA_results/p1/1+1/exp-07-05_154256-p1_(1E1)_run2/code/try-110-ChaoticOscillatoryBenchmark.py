import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 3.8  # Slightly reduced chaos parameter for better control
        self.freq = 6.0 * np.pi  # Increased frequency for more oscillations
        self.scale = 25.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance with modified log
            chaotic_factor = 1.0 + 0.5 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8))
        
        # Trigonometric oscillation component with modified frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) + np.sin(self.freq * x[i] * 0.7) * np.cos(self.freq * x[i] * 0.5)
        
        # Enhanced logistic map inspired interaction terms with quadratic coupling and cubic terms
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) + 0.1 * x[i]**3 * x[i+1]
        
        # Multi-scale oscillation with varying frequencies and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(18 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.12 * x[i]**4 + 0.06 * np.sin(25 * x[i])
        
        # Radial symmetry with polynomial decay and additional cosine term
        radial_symmetry = np.exp(-0.35 * r**2) * np.cos(self.freq * r) + 0.06 * r**3 + 0.03 * np.sin(12 * r)
        
        # Additional polynomial radial term for increased curvature
        poly_radial = 0.12 * r**4 + 0.06 * r**5
        
        # Add a new chaotic cross-term interaction between all dimensions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(self.r * x[i] * x[j]) * np.cos(self.r * x[i] * x[j] * 0.5)
        
        # Combine all components with adjusted weights
        return (0.35 * r**2 + 
                3.0 * trig_component + 
                0.55 * logistic_interaction + 
                1.1 * multi_scale + 
                0.3 * radial_symmetry + 
                0.2 * poly_radial + 
                0.3 * cross_term) * chaotic_factor