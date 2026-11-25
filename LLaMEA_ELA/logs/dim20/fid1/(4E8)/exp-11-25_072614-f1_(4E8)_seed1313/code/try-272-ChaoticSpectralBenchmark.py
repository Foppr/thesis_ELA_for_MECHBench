import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic system parameters with enhanced randomness
        self.chebyshev_coeffs = np.array([0.3 + 0.4 * np.sin(0.5 * np.pi * i) for i in range(dim)])
        # Precompute spectral graph laplacian eigenvalues with perturbed frequencies
        self.eigenvals = np.array([1.2 + 0.3 * np.cos(0.7 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system term with chebyshev polynomial mapping
        chaotic_term = 0.0
        for i in range(self.dim):
            coeff = self.chebyshev_coeffs[i]
            chaotic_term += (x[i]**2 + coeff * np.sin(4.0 * x[i])) * np.exp(-0.15 * x[i]**2)
        chaotic_term /= self.dim
        
        # Spectral graph theory term with laplacian eigenvalue modulation
        spectral_term = 0.0
        for i in range(self.dim):
            eigenval = self.eigenvals[i]
            spectral_term += (eigenval * np.cos(x[i]) + np.sin(eigenval * x[i])) * np.exp(-0.08 * x[i]**2)
        spectral_term /= self.dim
        
        # Adaptive penalty mechanism with multi-scale oscillation
        penalty_term = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.2 * np.cos(0.6 * np.pi * i)
            penalty_term += (scale * x[i]**4 - 2.5 * x[i]**2) * np.exp(-0.12 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with graph-theoretic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.4 * (i - j) + 0.3 * np.sum(x))
                cross_term += coupling * np.cos(x[i] + x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale chaotic basin structure with varying conditioning
        basin_term = 0.0
        for i in range(self.dim):
            basin_freq = 1.8 + 0.4 * np.sin(0.6 * np.pi * i)
            basin_term += (basin_freq * x[i]**3 - 2.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Temporal evolution with chaotic phase coupling
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.3 * np.cos(0.6 * np.pi * i + 0.15 * np.sum(x))
            temporal_term += np.sin(x[i] + phase) * np.exp(-0.12 * x[i]**2)
        temporal_term /= self.dim
        
        # Combined landscape with dynamic weighting based on spectral properties
        weights = np.abs(self.eigenvals) / np.sum(np.abs(self.eigenvals))
        
        total = (weights[0] * chaotic_term + 
                 weights[1] * spectral_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * basin_term + 
                 weights[5] * temporal_term)
        
        return total