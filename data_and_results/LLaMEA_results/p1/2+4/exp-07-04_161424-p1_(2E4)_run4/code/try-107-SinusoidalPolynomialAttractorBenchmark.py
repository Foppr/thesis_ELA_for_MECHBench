import numpy as np

class SinusoidalPolynomialAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency modulations and attraction centers
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.attraction_centers = np.random.uniform(-5.0, 5.0, (5, dim))
        self.polynomial_degrees = np.random.randint(3, 7, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        # Sinusoidal oscillation component
        sin_term = np.sum(np.sin(self.frequencies * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Polynomial potential with varying degrees
        poly_term = np.sum((x_norm**self.polynomial_degrees) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Gradient-based attraction fields
        attraction = 0.0
        for center in self.attraction_centers:
            dist = np.sum((x_norm - center/5.0)**2)
            attraction += np.exp(-dist / (2 * 0.3**2))
        
        # Multi-scale harmonic interference
        interference = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm))
        
        # Combine components with dynamic weights
        total = 0.4 * sin_term + 0.3 * poly_term + 0.2 * attraction + 0.1 * interference
        
        # Add conditioning via global scaling
        return total * (1 + 0.5 * np.tanh(np.sum(x_norm**3)))