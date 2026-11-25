import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly mutated fractal dimension scaling factors
        self.fractal_factors = np.array([1.0 + 0.3 * np.sin(0.7 * np.pi * i) for i in range(dim)])
        # Mutated quantum harmonic oscillator frequencies
        self.oscillator_freqs = np.array([1.3 + 0.25 * np.cos(0.5 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal geometry term with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            fractal_term += (x[i]**2 + scale * np.sin(3.8 * x[i])) * np.exp(-0.15 * x[i]**2)
        fractal_term /= self.dim
        
        # Quantum harmonic oscillator term with interference
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freqs[i]
            quantum_term += (freq * x[i]**2 - np.cos(freq * x[i])) * np.exp(-0.1 * x[i]**2)
        quantum_term /= self.dim
        
        # Temporal coupling with phase modulation
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.35 * np.sin(0.5 * np.pi * i + 0.2 * np.sum(x))
            temporal_term += np.sin(x[i] + phase) * np.cos(x[i] + phase) * np.exp(-0.15 * x[i]**2)
        temporal_term /= self.dim
        
        # Enhanced cross-dimensional fractal coupling with modified coupling strength
        cross_fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.85 + 0.15 * np.cos(0.35 * (i - j) + 0.45 * np.sum(x)) * np.exp(-0.1 * abs(i-j))
                cross_fractal += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_fractal /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale oscillation with quantum tunneling effect
        tunnel_term = 0.0
        for i in range(self.dim):
            tunnel_freq = 2.3 + 0.45 * np.sin(0.7 * np.pi * i)
            tunnel_term += np.sin(tunnel_freq * x[i]) * np.exp(-0.15 * x[i]**2) * (1.0 + 0.3 * np.cos(x[i]))
        tunnel_term /= self.dim
        
        # Self-similar basin structure with fractal dimension modulation
        basin_term = 0.0
        for i in range(self.dim):
            dim_factor = self.fractal_factors[i]
            basin_term += (dim_factor * x[i]**3 - 2.0 * x[i]) * np.exp(-0.12 * x[i]**2)
        basin_term /= self.dim
        
        # Quantum interference pattern with temporal evolution
        interference_term = 0.0
        for i in range(self.dim):
            interference_freq = 1.6 + 0.4 * np.cos(0.6 * np.pi * i)
            interference_term += np.sin(interference_freq * x[i]) * np.cos(interference_freq * x[i]) * np.exp(-0.1 * x[i]**2)
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