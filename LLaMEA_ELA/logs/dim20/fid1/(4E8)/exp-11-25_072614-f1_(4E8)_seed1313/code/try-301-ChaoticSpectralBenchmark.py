import numpy as np

class ChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spectral graph eigenvalues for coupling
        self.eigenvals = np.array([1.0 + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        # Precompute chaotic system parameters
        self.chaotic_params = np.array([0.8 + 0.2 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        # Precompute fractal basin scaling factors
        self.basin_factors = np.array([1.0 + 0.4 * np.sin(0.6 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical system term with logistic map influence
        chaotic_term = 0.0
        for i in range(self.dim):
            param = self.chaotic_params[i]
            chaotic_term += (param * x[i] * (1.0 - x[i]**2)) * np.exp(-0.1 * x[i]**2)
        chaotic_term /= self.dim
        
        # Spectral graph theory term with adjacency coupling
        spectral_term = 0.0
        for i in range(self.dim):
            eigenval = self.eigenvals[i]
            spectral_term += (eigenval * np.sin(x[i]) + 0.5 * np.cos(eigenval * x[i])) * np.exp(-0.08 * x[i]**2)
        spectral_term /= self.dim
        
        # Temporal phase modulation with adaptive coupling
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.4 * np.sin(0.5 * np.pi * i + 0.2 * np.sum(x))
            temporal_term += np.tan(x[i] + phase) * np.exp(-0.12 * x[i]**2)
        temporal_term /= self.dim
        
        # Enhanced cross-dimensional coupling with spectral weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.3 * np.cos(0.3 * (i - j) + 0.4 * np.sum(x))
                cross_coupling += weight * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        cross_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Fractal basin structure with adaptive scaling
        basin_term = 0.0
        for i in range(self.dim):
            factor = self.basin_factors[i]
            basin_term += (factor * x[i]**4 - 3.0 * x[i]**2) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Adaptive penalty mechanism with chaotic modulation
        penalty_term = 0.0
        for i in range(self.dim):
            penalty_factor = 1.0 + 0.3 * np.sin(0.8 * np.pi * i + 0.3 * np.sum(x))
            penalty_term += penalty_factor * (x[i]**2 - 5.0)**2 * np.exp(-0.06 * x[i]**2)
        penalty_term /= self.dim
        
        # Multi-scale oscillation with quantum-like interference
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.4 * np.cos(0.5 * np.pi * i)
            oscillation_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.09 * x[i]**2)
        oscillation_term /= self.dim
        
        # Novel coupling term with fractal dimension modulation
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(0.2 * (i + j) + 0.5 * np.sum(x))
                fractal_coupling += coupling_strength * np.cos(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        fractal_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Enhanced complexity with additional harmonic components
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.07 * x[i]**2)
        harmonic_term /= self.dim
        
        # Cross-dimensional nonlinear interaction with dynamic coupling
        nonlinear_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin(0.4 * (i - j) + 0.3 * np.sum(x))
                nonlinear_coupling += coupling_strength * np.tanh(x[i] * x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
        nonlinear_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combined term with dynamic weighting
        weights = np.abs(self.eigenvals) / np.sum(np.abs(self.eigenvals))
        
        total = (weights[0] * chaotic_term + 
                 weights[1] * spectral_term + 
                 weights[2] * temporal_term + 
                 weights[3] * cross_coupling + 
                 weights[4] * basin_term + 
                 weights[5] * penalty_term + 
                 weights[6] * oscillation_term +
                 0.15 * fractal_coupling +
                 0.1 * harmonic_term +
                 0.08 * nonlinear_coupling)
        
        return total