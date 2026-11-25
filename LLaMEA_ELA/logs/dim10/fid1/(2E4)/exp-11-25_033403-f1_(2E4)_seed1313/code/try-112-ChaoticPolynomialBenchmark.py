import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4.0
        self.sin_freq = 2.5
        self.radial_scale = 1.2
        self.chaos_factor = 0.7
        self.barrier_height = 2.0
        self.interaction_strength = 1.5
        self.rotation_angles = np.random.uniform(-np.pi, np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            degree = self.poly_degree * (1.0 + 0.3 * np.sin(i * 0.5))
            poly_term += x[i]**degree
            
        # Sinusoidal component with chaotic frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.sin_freq * (1.0 + self.chaos_factor * np.sin(i * 0.3 + x[i] * 0.1))
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Radial component with barrier structures
        radial_term = 0.0
        for i in range(self.dim):
            distance = np.abs(x[i])
            # Add barrier at specific points to create difficult regions
            barrier = self.barrier_height * (1.0 + np.exp(-distance * 2.0))
            radial_term += barrier * np.exp(-self.radial_scale * distance)
            
        # Cross-dimensional coupling with modified interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction with chaotic modulation
                interaction = self.interaction_strength * (1.0 + 0.2 * np.sin(i * 0.4 + j * 0.3))
                diff = x[i] - x[j]
                cross_term += interaction * np.sin(diff) * np.cos(diff)
                
        # Chaotic conditioning with dynamic scaling
        chaos_term = 0.0
        for i in range(self.dim):
            # Create chaotic behavior through nested sinusoids
            chaotic_component = np.sin(x[i]) + 0.5 * np.sin(2.0 * x[i]) + 0.3 * np.sin(3.0 * x[i])
            chaos_term += chaotic_component**2
            
        # Combined fitness function with balanced weights
        total = poly_term + sin_term + radial_term + cross_term + chaos_term
        
        return total