import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.radial_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.oscillation_freqs = np.random.uniform(1.0, 6.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multiple centers
        rbfs = 0.0
        for center in self.radial_centers:
            distance = np.sum((x - center) ** 2)
            rbfs += np.exp(-0.5 * distance) * np.sin(np.sqrt(distance))
        
        # Sinusoidal oscillation component with varying frequencies
        oscillations = 0.0
        for i in range(self.dim):
            oscillations += np.sin(self.oscillation_freqs[i] * x[i]) * np.cos(self.oscillation_freqs[i] * x[i]**2)
        
        # Gradient attraction fields creating valleys and ridges
        attraction = 0.0
        for i in range(self.dim):
            attraction += (x[i] ** 4 - 10 * x[i] ** 2 + 5 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-term interactions creating complex coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Asymmetric conditioning with polynomial scaling
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (x[i]**6 + 0.5 * x[i]**4 + 0.1 * x[i]**2) * np.exp(-0.02 * x[i]**2)
        
        # Combine all components with varying weights
        return 0.8 * rbfs + 1.5 * oscillations + 1.2 * attraction + 0.7 * cross_terms + 0.9 * conditioning