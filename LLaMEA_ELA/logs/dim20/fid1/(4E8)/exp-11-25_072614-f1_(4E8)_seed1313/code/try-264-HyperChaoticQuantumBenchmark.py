import numpy as np

class HyperChaoticQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute hyperchaotic system parameters with higher dimensionality
        self.hyper_coeffs = np.array([0.7 + 0.3 * np.cos(0.5 * np.pi * i) for i in range(dim)])
        # Precompute quantum spectral graph laplacian eigenvalues
        self.quantum_eigenvals = np.array([1.2 + 0.6 * np.sin(0.7 * np.pi * i) for i in range(dim)])
        # Precompute coupling strengths for quantum harmonic oscillators
        self.oscillator_couplings = np.array([0.8 + 0.2 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic dynamical system term with modified chebyshev polynomial mapping
        hyperchaos_term = 0.0
        for i in range(self.dim):
            coeff = self.hyper_coeffs[i]
            hyperchaos_term += (x[i]**3 + coeff * np.sin(7.0 * x[i])) * np.exp(-0.15 * x[i]**2)
        hyperchaos_term /= self.dim
        
        # Quantum spectral graph theory term with harmonic oscillator coupling
        quantum_term = 0.0
        for i in range(self.dim):
            eigenval = self.quantum_eigenvals[i]
            coupling = self.oscillator_couplings[i]
            quantum_term += (eigenval * np.cos(x[i]) + coupling * np.sin(eigenval * x[i])) * np.exp(-0.08 * x[i]**2)
        quantum_term /= self.dim
        
        # Adaptive penalty mechanism with multi-scale oscillation and quantum tunneling
        penalty_term = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.4 * np.sin(0.8 * np.pi * i)
            penalty_term += (scale * x[i]**5 - 3.0 * x[i]**3) * np.exp(-0.12 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with quantum graph-theoretic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.7 + 0.3 * np.sin(0.4 * (i - j) + 0.3 * np.sum(x))
                cross_term += coupling * np.cos(x[i] + x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale hyperchaotic basin structure with varying quantum conditioning
        basin_term = 0.0
        for i in range(self.dim):
            basin_freq = 2.0 + 0.5 * np.sin(0.6 * np.pi * i)
            basin_term += (basin_freq * x[i]**4 - 4.0 * x[i]**2) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Temporal evolution with quantum phase coupling and harmonic oscillation
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.cos(0.6 * np.pi * i + 0.15 * np.sum(x))
            temporal_term += np.sin(x[i] + phase) * np.exp(-0.12 * x[i]**2)
        temporal_term /= self.dim
        
        # Combined landscape with dynamic weighting based on quantum spectral properties
        weights = np.abs(self.quantum_eigenvals) / np.sum(np.abs(self.quantum_eigenvals))
        
        total = (weights[0] * hyperchaos_term + 
                 weights[1] * quantum_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * basin_term + 
                 weights[5] * temporal_term)
        
        return total