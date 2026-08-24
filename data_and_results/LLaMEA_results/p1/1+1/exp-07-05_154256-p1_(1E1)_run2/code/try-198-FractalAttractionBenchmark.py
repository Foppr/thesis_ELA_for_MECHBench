import numpy as np

class FractalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = 4
        self.attraction_strength = 2.0
        self.scale_factor = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fractal component
        fractal_value = 0.0
        for level in range(self.fractal_depth):
            scale = self.scale_factor ** level
            # Create fractal pattern using sine waves at different scales
            fractal_term = np.sum(np.sin(scale * x) * np.cos(scale * x * 0.5))
            fractal_value += fractal_term / (level + 1)
        
        # Gradient-based attraction fields
        attraction = 0.0
        for i in range(self.dim):
            # Attraction towards center with varying strength
            dist_to_center = np.abs(x[i])
            attraction += self.attraction_strength * np.exp(-0.5 * dist_to_center**2) * (1.0 + 0.3 * np.sin(3.0 * x[i]))
        
        # Multi-scale oscillation with varying amplitudes
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(10 * x[i]) * np.cos(5 * x[i]) * (1.0 + 0.2 * np.sin(2 * x[i]))
        
        # Polynomial curvature with cross-terms
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += 0.5 * x[i]**2 + 0.1 * x[i]**4
            for j in range(i+1, self.dim):
                polynomial += 0.05 * x[i] * x[j]
        
        # Combine all components
        return 0.5 * fractal_value + 0.3 * attraction + 0.2 * oscillation + 0.4 * polynomial