import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal dimension scaling factors with slight modification
        self.fractal_factors = np.array([1.0 + 0.35 * np.sin(0.65 * np.pi * i) for i in range(dim)])
        # Precompute quantum harmonic oscillator frequencies with adjustment
        self.oscillator_freqs = np.array([1.25 + 0.25 * np.cos(0.42 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal geometry term with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            fractal_term += (x[i]**2 + scale * np.sin(3.2 * x[i])) * np.exp(-0.11 * x[i]**2)
        fractal_term /= self.dim
        
        # Quantum harmonic oscillator term with interference
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freqs[i]
            quantum_term += (freq * x[i]**2 - np.cos(freq * x[i])) * np.exp(-0.055 * x[i]**2)
        quantum_term /= self.dim
        
        # Temporal coupling with phase modulation
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.42 * np.sin(0.52 * np.pi * i + 0.16 * np.sum(x))
            temporal_term += np.sin(x[i] + phase) * np.cos(x[i] + phase) * np.exp(-0.11 * x[i]**2)
        temporal_term /= self.dim
        
        # Enhanced cross-dimensional fractal coupling with modified coupling strength
        cross_fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.72 + 0.28 * np.cos(0.32 * (i - j) + 0.41 * np.sum(x)) * np.exp(-0.085 * abs(i-j))
                cross_fractal += coupling * np.sin(x[i] * x[j]) * np.exp(-0.055 * (x[i]**2 + x[j]**2))
        cross_fractal /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale oscillation with quantum tunneling effect
        tunnel_term = 0.0
        for i in range(self.dim):
            tunnel_freq = 2.55 + 0.38 * np.sin(0.72 * np.pi * i)
            tunnel_term += np.sin(tunnel_freq * x[i]) * np.exp(-0.105 * x[i]**2) * (1.0 + 0.32 * np.cos(x[i]))
        tunnel_term /= self.dim
        
        # Self-similar basin structure with fractal dimension modulation
        basin_term = 0.0
        for i in range(self.dim):
            dim_factor = self.fractal_factors[i]
            basin_term += (dim_factor * x[i]**3 - 2.45 * x[i]) * np.exp(-0.085 * x[i]**2)
        basin_term /= self.dim
        
        # Quantum interference pattern with temporal evolution
        interference_term = 0.0
        for i in range(self.dim):
            interference_freq = 1.85 + 0.38 * np.cos(0.62 * np.pi * i)
            interference_term += np.sin(interference_freq * x[i]) * np.cos(interference_freq * x[i]) * np.exp(-0.065 * x[i]**2)
        interference_term /= self.dim
        
        # Combined term with dynamic weighting based on fractal properties
        weights = np.abs(self.fractal_factors) / np.sum(np.abs(self.fractal_factors))
        
        total = (weights[0] * fractal_term + 
                 weights[1] * quantum_term + 
                 weights[2] * temporal_term + 
                 weights[3] * cross_fractal + 
                 weights[4] * tunnel_term + 
                 weights[5] * basin_term + 
                 weights[6] * interference_term)
        
        return total