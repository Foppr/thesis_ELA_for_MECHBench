import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Central quadratic attraction force
        quadratic_term = 0.1 * np.sum(x**2)
        
        # Exponentially decaying sinusoidal oscillations
        sinusoidal_term = 0.0
        for i in range(self.dim):
            # Create exponentially decaying amplitude
            amplitude = np.exp(-0.1 * (i + 1))
            # Add sinusoidal component with varying frequency
            frequency = 2.0 * (i + 1)
            sinusoidal_term += amplitude * np.sin(frequency * x[i])
        
        # Add a central repulsion force to create a single global minimum at origin
        repulsion_force = 0.0
        distance_from_origin = np.sqrt(np.sum(x**2))
        if distance_from_origin > 0:
            repulsion_force = 1.0 / (distance_from_origin * (1.0 + np.exp(-0.5 * distance_from_origin)))
        
        # Combine all terms with noise
        noise = 0.001 * np.sum(np.random.randn(self.dim))
        
        return quadratic_term - sinusoidal_term + repulsion_force + noise