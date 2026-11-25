import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic system parameters
        self.chebyshev_coeffs = np.array([0.5 + 0.3 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        # Precompute spectral graph eigenvalues
        self.eigenvals = np.array([1.0 + 0.4 * np.sin(0.6 * np.pi * i) for i in range(dim)])
        # Precompute adaptive penalty weights
        self.penalty_weights = np.array([0.7 + 0.3 * np.cos(0.5 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system term with chebyshev polynomial mapping
        chaotic_term = 0.0
        for i in range(self.dim):
            # Chebyshev polynomial chaos mapping
            T_n = np.cos(self.chebyshev_coeffs[i] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += (T_n**2 + 0.3 * np.sin(2.0 * x[i])) * np.exp(-0.1 * x[i]**2)
        chaotic_term /= self.dim
        
        # Spectral graph theory term with eigenvalue modulation
        spectral_term = 0.0
        for i in range(self.dim):
            # Graph Laplacian-like spectral component
            spectral_term += (self.eigenvals[i] * np.sin(x[i]) + 0.5 * np.cos(3.0 * x[i])) * np.exp(-0.08 * x[i]**2)
        spectral_term /= self.dim
        
        # Adaptive penalty mechanism with dynamic threshold
        penalty_term = 0.0
        for i in range(self.dim):
            # Penalty based on distance from feasible region
            dist_from_center = np.abs(x[i])
            penalty = self.penalty_weights[i] * (dist_from_center - 3.0)**2 * np.exp(-0.15 * dist_from_center)
            penalty_term += penalty
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with chaotic phase modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic phase coupling
                phase = np.sin(0.5 * np.pi * (i + j) + 0.2 * np.sum(x))
                coupling = 0.6 + 0.4 * np.cos(phase)
                cross_coupling += coupling * np.sin(x[i] + x[j]) * np.exp(-0.07 * (x[i]**2 + x[j]**2))
        cross_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale chaotic attractor with fractal basin structure
        attractor_term = 0.0
        for i in range(self.dim):
            # Logistic map-like chaotic behavior
            logistic_map = 4.0 * x[i] * (1.0 - x[i])
            attractor_term += (logistic_map**2 + 0.4 * np.sin(3.0 * x[i])) * np.exp(-0.12 * x[i]**2)
        attractor_term /= self.dim
        
        # Temporal evolution with spectral coherence
        temporal_term = 0.0
        for i in range(self.dim):
            # Time-varying spectral component
            time_phase = 0.3 * np.sin(0.7 * np.pi * i + 0.1 * np.sum(x))
            temporal_term += np.cos(x[i] + time_phase) * np.sin(x[i] + time_phase) * np.exp(-0.09 * x[i]**2)
        temporal_term /= self.dim
        
        # Combined objective with dynamic weighting
        weights = np.abs(np.array(self.eigenvals)) / np.sum(np.abs(np.array(self.eigenvals)))
        
        total = (weights[0] * chaotic_term + 
                 weights[1] * spectral_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_coupling + 
                 weights[4] * attractor_term + 
                 weights[5] * temporal_term)
        
        return total