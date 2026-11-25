import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with Gaussian-like behavior
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r**2) * np.sin(2 * np.pi * r)
        
        # Multi-modal sinusoidal structure
        sin_term = np.sum(np.sin(3 * x + np.pi/4) * np.cos(2 * x - np.pi/6))
        
        # Polynomial conditioning with variable exponents
        poly_term = np.sum((x**4 + 0.5 * x**3 - 0.8 * x**2 + 1.2 * x + 0.5)**1.1)
        
        # Chaotic modulation using logistic map-inspired terms
        chaotic_term = np.sum(np.sin(10 * np.sin(x)) * np.cos(7 * np.cos(x)))
        
        # Cross-term interactions for increased complexity
        cross_term = np.sum((x[:-1] * x[1:])**(1.5) if self.dim > 1 else 0)
        
        # Combine all components with adaptive weights
        return 0.3 * radial_term + 0.25 * sin_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.1 * cross_term + 1.0