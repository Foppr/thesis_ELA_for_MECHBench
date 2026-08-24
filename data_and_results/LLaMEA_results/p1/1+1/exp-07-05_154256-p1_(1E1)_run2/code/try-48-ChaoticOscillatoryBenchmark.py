import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for enhanced chaotic behavior
        self.r = 4.0  # Increased chaos parameter
        self.freq = 4.0 * np.pi  # Further increased frequency for more oscillations
        self.scale = 15.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply enhanced chaotic scaling based on radial distance with modified log and sine
            chaotic_factor = 1.0 + 0.8 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.sqrt(r))
        
        # Trigonometric oscillation component with modified frequencies and cross-dimensional terms
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) + 0.5 * np.sin(2 * self.freq * x[i])
        
        # Enhanced logistic map inspired interaction terms with cubic coupling and cross-dimensionality
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) * np.cos(0.5 * x[i+1])
            if i < self.dim - 2:
                logistic_interaction += 0.3 * x[i] * x[i+1] * x[i+2] * (self.r * x[i] * (1 - x[i]**3))
        
        # Multi-scale oscillation with varying frequencies, additional polynomial terms, and exponential decay
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.1 * x[i]**4 + 0.05 * np.sin(20 * x[i]**2)
        
        # Radial symmetry with polynomial decay, additional cosine term, and cross-dimensional interaction
        radial_symmetry = np.exp(-0.3 * r**2) * np.cos(self.freq * r) + 0.05 * r**3 + 0.2 * np.sin(3 * r)
        
        # Additional polynomial radial term for increased curvature and cross-dimensional coupling
        poly_radial = 0.1 * r**4 + 0.05 * r**5 * np.cos(0.5 * r)
        
        # Cross-dimensional coupling term with chaotic interaction
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.1 * np.sin(self.r * x[i] * x[j]) * np.cos(self.r * (x[i]**2 + x[j]**2))
        
        # Combine all components with adjusted weights
        return (0.4 * r**2 + 
                2.5 * trig_component + 
                0.6 * logistic_interaction + 
                0.9 * multi_scale + 
                0.3 * radial_symmetry + 
                0.15 * poly_radial + 
                0.2 * cross_coupling) * chaotic_factor