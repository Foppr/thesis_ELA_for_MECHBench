import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for higher complexity
        self.r = 3.95  # Increased chaos parameter
        self.freq = 4.2 * np.pi  # Higher frequency for more intricate oscillations
        self.scale = 15.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Apply enhanced chaotic scaling with multiple logistic maps
            chaotic_factor = 1.0 + 0.7 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.sqrt(r))
        
        # Trigonometric oscillation component with nested frequencies and coupling
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) * np.sin(self.freq * x[i] * 0.7)
        
        # Enhanced logistic map inspired interaction terms with cubic coupling and cross-dimensionality
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2)) * np.sin(x[i+1])
        
        # Multi-scale oscillation with varying frequencies, exponential decay, and polynomial coupling
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(20 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.15 * x[i]**5 + 0.05 * x[i]**3
        
        # Radial symmetry with polynomial decay, multiple cosine terms, and additional chaotic modulation
        radial_symmetry = np.exp(-0.4 * r**2) * np.cos(self.freq * r) * np.sin(0.5 * r) + 0.08 * r**4 + 0.03 * r**6
        
        # Additional polynomial radial term with higher degree and chaotic scaling
        poly_radial = 0.12 * r**5 + 0.05 * r**7
        
        # Cross-dimensional coupling with sine and cosine interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (1.0 + 0.1 * np.sin(r))
        
        # Combine all components with adjusted weights and enhanced chaotic modulation
        return (0.5 * r**2 + 
                3.0 * trig_component + 
                0.8 * logistic_interaction + 
                1.2 * multi_scale + 
                0.4 * radial_symmetry + 
                0.2 * poly_radial + 
                0.1 * cross_coupling) * chaotic_factor