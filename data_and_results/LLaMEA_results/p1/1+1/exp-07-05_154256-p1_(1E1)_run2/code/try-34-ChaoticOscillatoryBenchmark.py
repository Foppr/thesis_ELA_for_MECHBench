import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.r = 3.95  # Increased chaos parameter
        self.freq = 4.2 * np.pi  # Higher frequency for more intricate oscillations
        self.scale = 15.0
        # Additional fractal-like constants
        self.fractal_dim = 1.7
        self.coupling_strength = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Fractal-inspired chaotic scaling
            chaotic_factor = 1.0 + 0.7 * np.sin(self.r * np.log(r + 1e-8)) * np.cos(self.r * np.log(r + 1e-8) * 0.5)
        
        # Enhanced trigonometric oscillation with nested frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3) * np.sin(self.freq * x[i] * 0.7)
        
        # Cross-dimensional chaotic coupling with higher-order polynomial interactions
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] * x[j]) * (self.r * x[i] * (1 - x[i]**2)) * (self.r * x[j] * (1 - x[j]**2))
        
        # Multi-scale oscillation with fractal-like behavior and exponential decay
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += (np.sin(20 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.2 * x[i]**2) + 
                           0.15 * x[i]**6) * np.sin(self.fractal_dim * np.log(np.abs(x[i]) + 1e-8))
        
        # Radial symmetry with fractal dimension scaling and additional cosine terms
        radial_symmetry = np.exp(-0.4 * r**2) * np.cos(self.freq * r) * np.sin(self.fractal_dim * r) + 0.08 * r**5
        
        # Additional polynomial radial term with fractal curvature
        poly_radial = 0.12 * r**6
        
        # Nested chaotic component with recursive structure
        nested_chaos = 0
        for i in range(self.dim):
            nested_chaos += np.sin(self.r * np.sin(self.r * x[i])) * np.cos(self.r * np.cos(self.r * x[i]))
        
        # Combine all components with adjusted weights for maximum complexity
        return (0.5 * r**2 + 
                3.0 * trig_component + 
                0.8 * coupling_term + 
                1.2 * multi_scale + 
                0.4 * radial_symmetry + 
                0.2 * poly_radial + 
                0.3 * nested_chaos) * chaotic_factor