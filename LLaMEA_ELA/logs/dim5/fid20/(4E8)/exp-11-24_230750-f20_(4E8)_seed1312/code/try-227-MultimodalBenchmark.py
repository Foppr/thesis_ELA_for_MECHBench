import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal recursive tangent interactions with self-similar basins
        fractal_tangent = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                fractal_tangent += np.tan(dist * (1 + 0.3 * np.sin(i * j))) * np.cos(3 * dist)
        
        # Self-similar basin structures with logarithmic penalties
        basin_structures = 0.0
        for i in range(self.dim):
            basin_pos = 2.5 * np.cos(i * np.pi / (self.dim + 1))
            basin_width = 0.5 + 0.3 * np.sin(i * np.pi / self.dim)
            basin_height = 2.0 + 0.8 * np.cos(i * np.pi / (self.dim + 2))
            basin_structures += basin_height * np.exp(-0.5 * ((x[i] - basin_pos) ** 2) / (basin_width ** 2)) * np.sin(5 * x[i])
        
        # Logarithmic barrier penalties with dynamic scaling
        log_penalties = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                log_penalties += np.log(np.abs(x[i]) - 4.0) * np.exp(-0.3 * x[i]**2)
            elif np.abs(x[i]) > 3.5:
                log_penalties += np.log(np.abs(x[i]) - 3.0) * np.cos(2 * x[i])
        
        # Dynamic frequency modulation with adaptive scaling
        freq_modulation = 0.0
        for i in range(self.dim):
            freq = 2 + 1.5 * np.sin(i * 0.7) + 0.8 * np.cos(i * 0.3)
            freq_modulation += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.02 * i)
        
        # Cross-dimensional exponential interactions with phase coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.cos(i * j * 0.4) + 0.5 * np.sin(i + j)
                cross_exp += np.exp(-np.abs(x[i] - x[j])) * np.sin(x[i] + x[j] + phase)
        
        # Nested harmonic oscillations with variable amplitudes
        nested_harmonics = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.4 * np.sin(i * 0.6)
            freq = 1.5 + 0.8 * np.cos(i * 0.4)
            nested_harmonics += amp * np.sin(freq * x[i]) * np.cos(3 * freq * x[i])
        
        # Quantum-like probability distributions with multi-scale peaks
        quantum_prob = 0.0
        for i in range(self.dim):
            peak_pos = 4.0 * np.sin(i * np.pi / (self.dim + 1))
            width = 0.6 + 0.3 * np.cos(i * np.pi / self.dim)
            height = 1.8 + 0.7 * np.sin(i * np.pi / (self.dim + 2))
            quantum_prob += height * np.exp(-0.5 * ((x[i] - peak_pos) ** 2) / (width ** 2)) * np.cos(6 * x[i])
        
        # Combined fitness with enhanced weights and dynamic scaling
        return 0.25 * fractal_tangent + 0.2 * basin_structures + 0.15 * log_penalties + 0.15 * freq_modulation + 0.1 * cross_exp + 0.08 * nested_harmonics + 0.07 * quantum_prob