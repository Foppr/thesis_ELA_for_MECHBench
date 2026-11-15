import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 4.1  # Increased chaos parameter for higher complexity
        self.freq = 7.0 * np.pi  # Further increased frequency for more oscillations
        self.scale = 25.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply enhanced chaotic scaling with double logistic modulation
            chaotic_factor = 1.0 + 0.8 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8)) + \
                              0.4 * np.sin(self.r * np.log(r + 1e-8) * 2) * np.cos(self.r * np.log(r + 1e-8) * 2)
        
        # Trigonometric oscillation component with enhanced frequencies and coupling
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) + \
                             np.sin(self.freq * x[i] * 0.7) * np.cos(self.freq * x[i] * 0.5) + \
                             0.5 * np.sin(self.freq * x[i] * 1.3) * np.cos(self.freq * x[i] * 0.8)
        
        # Enhanced logistic map inspired interaction terms with higher-order coupling and cubic terms
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) + \
                                       0.1 * x[i]**3 * x[i+1] + \
                                       0.05 * x[i]**2 * x[i+1]**2
        
        # Multi-scale oscillation with varying frequencies, additional polynomial terms and exponential decay
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.15 * x[i]**2) + \
                           0.1 * x[i]**4 + 0.05 * np.sin(20 * x[i]) + \
                           0.03 * np.sin(25 * x[i]) * np.cos(10 * x[i])
        
        # Radial symmetry with polynomial decay, additional cosine term and enhanced exponential
        radial_symmetry = np.exp(-0.3 * r**2) * np.cos(self.freq * r) + 0.05 * r**3 + 0.02 * np.sin(10 * r) + \
                          0.01 * np.exp(-0.5 * r**3)
        
        # Additional polynomial radial term for increased curvature and higher-order terms
        poly_radial = 0.1 * r**4 + 0.05 * r**5 + 0.02 * r**6
        
        # Add a new chaotic cross-term interaction between all dimensions with higher-order coupling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(self.r * x[i] * x[j]) * np.cos(self.r * x[i] * x[j] * 0.5) + \
                              0.3 * np.sin(self.r * x[i] * x[j] * 0.3) * np.cos(self.r * x[i] * x[j] * 0.7) + \
                              0.1 * np.sin(self.r * x[i]**2 * x[j]**2) * np.cos(self.r * x[i]**2 * x[j]**2 * 0.2)
        
        # Combine all components with adjusted weights for increased complexity
        return (0.3 * r**2 + 
                3.2 * trig_component + 
                0.6 * logistic_interaction + 
                1.2 * multi_scale + 
                0.3 * radial_symmetry + 
                0.2 * poly_radial + 
                0.3 * cross_term) * chaotic_factor