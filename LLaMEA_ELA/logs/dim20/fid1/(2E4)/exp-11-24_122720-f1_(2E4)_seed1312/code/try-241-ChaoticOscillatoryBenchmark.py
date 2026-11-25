import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic coupling coefficients
        self.coupling_coeffs = [0.5 * (1 + np.sin(i * np.pi / (dim + 3))) for i in range(dim)]
        self.oscillation_freqs = [1.0 + 0.5 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.cross_coupling = [[0.3 * np.sin(i * j * np.pi / (dim + 1)) for j in range(dim)] for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic component with chaotic modulation
        norm = np.linalg.norm(x)
        if norm > 0:
            radial_term = (norm**2) * (1 + 0.2 * np.sin(3 * norm))
        else:
            radial_term = 0
            
        # Sinusoidal oscillations with dimension-specific frequencies
        oscillation_term = 0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i]
            oscillation_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional chaotic couplings
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.cross_coupling[i][j]
                cross_term += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Chaotic perturbation components
        chaos_term = 0
        for i in range(self.dim):
            perturbation = 0.1 * np.sin(i * np.pi / (self.dim + 5)) * np.cos(i * np.pi / (self.dim + 6))
            chaos_term += (x[i]**2 + perturbation) * (1 + 0.1 * np.sin(i * np.pi / (self.dim + 4)))
            
        # Dimensional scaling with chaotic factors
        scale_factor = 1.0 + 0.2 * np.sum([np.sin(i * np.pi / (self.dim + 1)) for i in range(self.dim)])
        
        # Combine all terms
        return scale_factor * (radial_term + oscillation_term + cross_term + chaos_term) + 0.05 * self.dim