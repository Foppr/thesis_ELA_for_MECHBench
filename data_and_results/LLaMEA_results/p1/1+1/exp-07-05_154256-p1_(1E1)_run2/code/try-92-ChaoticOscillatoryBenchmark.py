import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 4.0  # Increased chaos parameter for stronger chaos
        self.freq = 4.0 * np.pi  # Higher frequency for more oscillations
        self.scale = 15.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply chaotic scaling based on radial distance with modified log
            chaotic_factor = 1.0 + 0.7 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8))
        
        # Trigonometric oscillation component with modified frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) + 0.3 * np.sin(2 * self.freq * x[i])
        
        # Enhanced logistic map inspired interaction terms with quadratic coupling
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) + 0.2 * x[i]**3 * x[i+1]
        
        # Multi-scale oscillation with varying frequencies and additional polynomial terms
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.1 * x[i]**4 + 0.05 * np.sin(20 * x[i])
        
        # Radial symmetry with polynomial decay and additional cosine term
        radial_symmetry = np.exp(-0.3 * r**2) * np.cos(self.freq * r) + 0.05 * r**3 + 0.1 * np.sin(5 * r)
        
        # Additional polynomial radial term for increased curvature
        poly_radial = 0.1 * r**4 + 0.05 * r**6
        
        # Multi-modal component with additional chaotic peaks
        modal_component = 0
        for i in range(self.dim):
            modal_component += 0.5 * np.sin(10 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.3 * np.sin(30 * x[i])
        
        # Combine all components with adjusted weights
        return (0.4 * r**2 + 
                2.5 * trig_component + 
                0.6 * logistic_interaction + 
                0.9 * multi_scale + 
                0.3 * radial_symmetry + 
                0.15 * poly_radial + 
                0.2 * modal_component) * chaotic_factor