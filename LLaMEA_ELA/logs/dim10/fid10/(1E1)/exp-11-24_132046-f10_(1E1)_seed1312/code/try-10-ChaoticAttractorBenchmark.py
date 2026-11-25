import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial quadratic basin term
        radial_term = np.sum(x_norm**2)
        
        # Sinusoidal modulation with chaotic frequency progression
        freqs = np.arange(1, self.dim + 1) * np.pi / 4
        sin_mod = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-abs(x_norm[i] - x_norm[i+1])) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Multi-scale periodic component with varying amplitudes
        periodic = 0.5 * np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * np.sin(3 * x_norm))
        
        # Chaotic attractor term using a logistic-like map
        chaotic = 0.3 * np.sum(np.sin(np.pi * (x_norm**3 + 0.5 * x_norm)) * np.cos(np.pi * (x_norm**2)))
        
        # Asymmetric curvature with hinge-like behavior
        hinge = 0.2 * np.sum(np.maximum(0, x_norm)**3 + np.maximum(0, -x_norm)**4)
        
        return radial_term + sin_mod + coupling + periodic + chaotic + hinge