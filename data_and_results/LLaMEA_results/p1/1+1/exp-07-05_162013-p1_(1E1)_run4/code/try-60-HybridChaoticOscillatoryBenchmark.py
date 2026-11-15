import numpy as np

class HybridChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = np.random.uniform(1.0, 10.0, dim)
        self.oscillation_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.basis_centers = np.random.uniform(-3.0, 3.0, (5, dim))
        self.basis_weights = np.random.uniform(0.5, 2.0, 5)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        oscillation = np.sum(np.sin(self.oscillation_frequencies * x) * np.cos(self.oscillation_frequencies * x))
        
        # Radial basis function component
        rbf = 0.0
        for i in range(5):
            diff = x - self.basis_centers[i]
            rbf += self.basis_weights[i] * np.exp(-np.sum((diff / self.conditioning)**2))
        
        # Adaptive conditioning component
        conditioning_term = np.sum(self.conditioning * x**2)
        
        # Cross-term coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Global minimum attraction
        global_attraction = np.sum(x**2)
        
        # Noise modulation
        noise = 0.01 * np.sum(np.sin(10 * x))
        
        return oscillation + rbf + conditioning_term + coupling + global_attraction + noise