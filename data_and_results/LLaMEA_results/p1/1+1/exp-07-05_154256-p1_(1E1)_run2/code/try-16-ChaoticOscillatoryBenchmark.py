import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 3.9  # Increased chaos parameter
        self.freq = 4.0 * np.pi  # Further increased frequency for more oscillations
        self.scale = 15.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance with modified log
            chaotic_factor = 1.0 + 0.7 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.sqrt(r))
        
        # Trigonometric oscillation component with perturbed frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i] * (1 + 0.1 * np.sin(0.5 * x[i]))) * np.cos(self.freq * x[i] * 0.3 * (1 + 0.05 * np.cos(0.7 * x[i])))
        
        # Enhanced logistic map inspired interaction terms with cubic coupling and cross-dimensionality
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1] * (x[i] + x[i+1])) * (self.r * x[i] * (1 - x[i]**2))
        
        # Multi-scale oscillation with varying frequencies, exponential decay, and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(20 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.15 * x[i]**5
        
        # Radial symmetry with polynomial decay and additional cosine term with higher frequency
        radial_symmetry = np.exp(-0.4 * r**2) * np.cos(self.freq * r) + 0.07 * r**4 + 0.03 * np.sin(10 * r)
        
        # Additional polynomial radial term for increased curvature and nonlinearity
        poly_radial = 0.15 * r**5
        
        # Cross-dimensional coupling term with sine modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(2 * x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Combine all components with adjusted weights
        return (0.5 * r**2 + 
                3.0 * trig_component + 
                0.8 * logistic_interaction + 
                1.1 * multi_scale + 
                0.4 * radial_symmetry + 
                0.2 * poly_radial + 
                0.25 * cross_coupling) * chaotic_factor