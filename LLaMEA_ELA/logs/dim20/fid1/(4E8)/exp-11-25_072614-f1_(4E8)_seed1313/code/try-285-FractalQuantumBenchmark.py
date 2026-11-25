import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like chaotic parameters with quantum-inspired frequencies
        self.fractal_params = np.array([0.7 + 0.3 * np.sin(0.8 * np.pi * i) for i in range(dim)])
        # Precompute quantum harmonic oscillator eigenfrequencies with perturbed coupling
        self.oscillator_freqs = np.array([1.5 + 0.4 * np.cos(0.9 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like chaotic system with quantum harmonic oscillator coupling
        fractal_term = 0.0
        for i in range(self.dim):
            param = self.fractal_params[i]
            fractal_term += (x[i]**2 + param * np.sin(3.0 * x[i])) * np.exp(-0.2 * x[i]**2)
        fractal_term /= self.dim
        
        # Quantum harmonic oscillator term with modified potential
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freqs[i]
            quantum_term += (freq * np.cos(x[i]) + np.sin(freq * x[i])) * np.exp(-0.15 * x[i]**2)
        quantum_term /= self.dim
        
        # Adaptive penalty mechanism with multi-scale oscillation and fractal modulation
        penalty_term = 0.0
        for i in range(self.dim):
            scale = 1.5 + 0.3 * np.cos(0.8 * np.pi * i)
            penalty_term += (scale * x[i]**4 - 3.0 * x[i]**2) * np.exp(-0.18 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with fractal interaction structure
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.4 * np.sin(0.5 * (i - j) + 0.4 * np.sum(x))
                cross_term += coupling * np.cos(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Fractal basin structure with quantum phase coupling
        basin_term = 0.0
        for i in range(self.dim):
            basin_freq = 2.0 + 0.5 * np.sin(0.7 * np.pi * i)
            basin_term += (basin_freq * x[i]**3 - 3.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        basin_term /= self.dim
        
        # Temporal evolution with quantum phase modulation
        temporal_term = 0.0
        for i in range(self.dim):
            phase = 0.4 * np.cos(0.7 * np.pi * i + 0.2 * np.sum(x))
            temporal_term += np.sin(x[i] + phase) * np.exp(-0.15 * x[i]**2)
        temporal_term /= self.dim
        
        # Combined landscape with dynamic weighting based on fractal properties
        weights = np.abs(self.oscillator_freqs) / np.sum(np.abs(self.oscillator_freqs))
        
        total = (weights[0] * fractal_term + 
                 weights[1] * quantum_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * basin_term + 
                 weights[5] * temporal_term)
        
        return total