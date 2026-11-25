import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic system parameters with enhanced complexity
        self.chebyshev_coeffs = np.array([0.7 + 0.4 * np.cos(0.5 * np.pi * i) for i in range(dim)])
        # Precompute spectral graph laplacian eigenvalues with non-uniform distribution
        self.eigenvals = np.array([1.2 + 0.6 * np.sin(0.7 * np.pi * i) for i in range(dim)])
        # Add temporal phase coupling coefficients
        self.phase_coeffs = np.array([0.3 + 0.2 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system term with chebyshev polynomial mapping and enhanced nonlinearity
        chaotic_term = 0.0
        for i in range(self.dim):
            coeff = self.chebyshev_coeffs[i]
            chaotic_term += (x[i]**3 + coeff * np.cos(6.0 * x[i]) + 0.5 * np.sin(3.0 * x[i])) * np.exp(-0.12 * x[i]**2)
        chaotic_term /= self.dim
        
        # Spectral graph theory term with laplacian eigenvalue modulation and multi-scale frequency
        spectral_term = 0.0
        for i in range(self.dim):
            eigenval = self.eigenvals[i]
            spectral_term += (eigenval * np.sin(1.5 * x[i]) + np.cos(eigenval * x[i]) + 0.3 * np.tan(0.5 * x[i])) * np.exp(-0.06 * x[i]**2)
        spectral_term /= self.dim
        
        # Adaptive penalty mechanism with multi-scale oscillation and enhanced conditioning
        penalty_term = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.4 * np.sin(0.8 * np.pi * i)
            penalty_term += (scale * x[i]**5 - 3.0 * x[i]**3 + 2.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with graph-theoretic interaction and enhanced nonlinearity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.8 + 0.2 * np.cos(0.5 * (i - j) + 0.4 * np.sum(x)) * np.sin(0.3 * x[i])
                cross_term += coupling * np.sin(1.5 * x[i] + x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale chaotic basin structure with varying conditioning and enhanced complexity
        basin_term = 0.0
        for i in range(self.dim):
            basin_freq = 2.0 + 0.8 * np.cos(0.6 * np.pi * i)
            basin_term += (basin_freq * x[i]**4 - 4.0 * x[i]**2 + 1.0) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Temporal evolution with chaotic phase coupling and enhanced modulation
        temporal_term = 0.0
        for i in range(self.dim):
            phase = self.phase_coeffs[i] * np.sin(0.6 * np.pi * i + 0.15 * np.sum(x))
            temporal_term += np.tan(1.2 * x[i] + phase) * np.exp(-0.12 * x[i]**2)
        temporal_term /= self.dim
        
        # Additional fractal-like structure term with enhanced dimensionality coupling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_freq = 1.8 + 0.4 * np.sin(0.3 * np.pi * i)
            fractal_term += (fractal_freq * np.sin(x[i]) + 0.6 * np.cos(2.0 * x[i])) * np.exp(-0.07 * x[i]**2)
        fractal_term /= self.dim
        
        # Combined landscape with dynamic weighting based on spectral properties and enhanced complexity
        weights = np.abs(self.eigenvals) / np.sum(np.abs(self.eigenvals))
        
        total = (weights[0] * chaotic_term + 
                 weights[1] * spectral_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * basin_term + 
                 weights[5] * temporal_term + 
                 weights[6] * fractal_term)
        
        return total