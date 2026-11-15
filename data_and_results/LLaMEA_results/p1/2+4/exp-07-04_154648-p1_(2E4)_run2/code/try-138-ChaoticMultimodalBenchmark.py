import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.harmonic_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.penalty_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.penalty_radii = np.random.uniform(0.5, 2.0, 10)
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.adaptive_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        t = np.sum(x_norm) % (2 * np.pi)
        
        # Chaotic harmonic potential with time-varying phase
        harmonic_potential = 0.0
        for i in range(self.dim):
            phase = self.time_phase[i] + t * 0.1
            harmonic_potential += (np.sin(self.harmonic_frequencies[i] * x_norm[i] + phase) * 
                                 np.cos(self.harmonic_frequencies[i] * x_norm[i] * 1.3 + phase)) * \
                                self.adaptive_weights[i]
        
        # Adaptive penalty regions with dynamic radii
        penalty = 0.0
        for i in range(10):
            diff = x_norm - self.penalty_centers[i]
            radius = self.penalty_radii[i] * (1.0 + 0.2 * np.sin(t))
            dist = np.sqrt(np.sum(diff**2))
            if dist < radius:
                penalty += 10.0 * (radius - dist)**2
        
        # Cross-dimensional coupling with chaotic interaction
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling += np.sin(x_norm[i] * x_norm[j] + t * 0.5) * \
                       np.cos(x_norm[i] + x_norm[j] + t * 0.3) * \
                       (1.0 + 0.1 * np.sin(3 * t))
        
        # Polynomial and chaotic noise components
        poly_term = 0.05 * np.sum(x_norm**6)
        noise = 0.03 * np.sum(np.sin(10 * x_norm + t) * np.cos(7 * x_norm + t))
        
        # Combine all terms
        return harmonic_potential + penalty + coupling + poly_term + noise