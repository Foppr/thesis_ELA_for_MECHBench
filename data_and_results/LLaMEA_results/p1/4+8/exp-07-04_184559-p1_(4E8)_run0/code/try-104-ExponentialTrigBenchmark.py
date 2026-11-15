import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute trigonometric coefficients for coupling
        self.freqs = np.arange(1, dim + 1)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential barrier component with multiple local minima
        barriers = np.sum(self.amps * np.exp(-0.5 * (x_norm**2) / (0.1 + np.abs(x_norm))))
        
        # Trigonometric coupling terms creating complex interaction patterns
        trig_coupling = np.sum(np.sin(self.freqs * x_norm) * np.cos(self.freqs * x_norm**2))
        
        # Adaptive conditioning based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x_norm**2))
        conditioning = 1 + 0.5 * np.sin(dist_from_origin * np.pi)
        
        # Polynomial interaction with varying exponents
        poly_interaction = np.sum((x_norm**4 + 0.3 * x_norm**3 - 0.1 * x_norm**2 + 0.05 * x_norm)**2)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                               (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # High-frequency oscillation component
        high_freq = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Combine all components with dynamic weights
        return 1.2 * barriers + 0.9 * trig_coupling + 0.7 * conditioning * poly_interaction + \
               0.5 * cross_coupling + 0.8 * high_freq