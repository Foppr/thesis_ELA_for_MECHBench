import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimension parameters with chaotic perturbations
        self.fractal_dims = np.array([1.5 + 0.3 * np.sin(0.8 * np.pi * i) for i in range(dim)])
        # Precompute quantum oscillator frequencies with temporal modulation
        self.frequencies = np.array([2.0 + 0.5 * np.cos(0.6 * np.pi * i) for i in range(dim)])
        # Precompute coupling strengths with fractal scaling
        self.coupling_strengths = np.array([0.7 + 0.3 * np.sin(0.9 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal geometry term with multi-scale self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            dim_factor = self.fractal_dims[i]
            fractal_term += (x[i]**2 + np.sin(dim_factor * x[i])) * np.exp(-0.1 * x[i]**2)
        fractal_term /= self.dim
        
        # Quantum harmonic oscillator term with frequency modulation
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i]
            quantum_term += (freq * np.cos(x[i]) + np.sin(freq * x[i])) * np.exp(-0.05 * x[i]**2)
        quantum_term /= self.dim
        
        # Temporal coupling with phase synchronization
        temporal_coupling = 0.0
        for i in range(self.dim):
            phase = 0.4 * np.cos(0.7 * np.pi * i + 0.2 * np.sum(x))
            temporal_coupling += np.sin(x[i] + phase) * np.exp(-0.15 * x[i]**2)
        temporal_coupling /= self.dim
        
        # Cross-dimensional coupling with fractal interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                cross_term += coupling * np.cos(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Modified interaction terms with enhanced nonlinearity
        interaction_term = 0.0
        for i in range(self.dim):
            interaction_term += (x[i]**3 + 0.5 * np.sin(2.0 * x[i]) + 0.3 * np.cos(1.5 * x[i])) * np.exp(-0.08 * x[i]**2)
        interaction_term /= self.dim
        
        # Enhanced basin structure with quantum tunneling effects
        basin_term = 0.0
        for i in range(self.dim):
            tunnel_freq = 1.2 + 0.4 * np.sin(0.5 * np.pi * i)
            basin_term += (tunnel_freq * x[i]**4 - 3.0 * x[i]**2) * np.exp(-0.12 * x[i]**2)
        basin_term /= self.dim
        
        # Combined landscape with dynamic weighting based on fractal properties
        weights = np.abs(self.fractal_dims) / np.sum(np.abs(self.fractal_dims))
        
        total = (weights[0] * fractal_term + 
                 weights[1] * quantum_term + 
                 weights[2] * temporal_coupling + 
                 weights[3] * cross_term + 
                 weights[4] * interaction_term + 
                 weights[5] * basin_term)
        
        return total