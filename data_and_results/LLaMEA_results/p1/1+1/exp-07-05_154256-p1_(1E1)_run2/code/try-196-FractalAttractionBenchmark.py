import numpy as np

class FractalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = 4
        self.attraction_strength = 2.0
        self.periodic_factor = 3.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like self-similarity component
        for d in range(self.fractal_depth):
            scale = 2.0 ** d
            # Apply fractal scaling with sinusoidal modulation
            fractal_term = np.sum(np.sin(scale * x) * np.cos(scale * x * 0.5))
            result += 0.5 * (1.0 / (d + 1)) * fractal_term
        
        # Gradient-based attraction field
        attraction_field = 0.0
        for i in range(self.dim):
            # Create attractive points in the search space
            attractor_positions = np.array([-3.0, -1.0, 1.0, 3.0])
            for pos in attractor_positions:
                distance = np.abs(x[i] - pos)
                attraction_field += self.attraction_strength * np.exp(-0.5 * (distance / 0.5)**2)
        
        # Periodic boundary interactions
        periodic_interaction = 0.0
        for i in range(self.dim):
            periodic_interaction += np.sin(self.periodic_factor * x[i]) * np.cos(self.periodic_factor * x[i] * 0.3)
        
        # Radial polynomial component with mixed curvature
        r = np.sqrt(np.sum(x**2))
        radial_component = 0.1 * r**6 + 0.3 * r**4 + 0.5 * r**2
        
        # Cross-dimensional coupling with exponential interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2.0 * x[i] * x[j])
        
        # Combine all components with adaptive weights
        total = (1.5 * result + 
                 2.0 * attraction_field + 
                 1.2 * periodic_interaction + 
                 0.8 * radial_component + 
                 0.6 * cross_coupling)
        
        # Add noise term for increased complexity
        noise = 0.05 * np.random.random()
        
        return total + noise