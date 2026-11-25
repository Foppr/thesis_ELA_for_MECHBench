import numpy as np

class NestedFractalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic coupling parameters
        self.chaos_factor = 3.2
        self.coupling_strength = 1.2
        # Modified fractal scaling with nested structure
        self.fractal_exp = 1.5
        self.scale_base = 1.8
        # Quantum-inspired interference patterns
        self.quantum_amp = 0.7
        self.quantum_freq = 6.0 * np.pi
        # Ruggedness control with dynamic scaling
        self.ruggedness = 0.05
        # Nested basin parameters
        self.nest_levels = 3
        self.basin_strength = 2.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Nested fractal basin structure with multiple levels
        basin_energy = 0.0
        for i in range(self.dim):
            level_energy = 0.0
            for level in range(self.nest_levels):
                scale_factor = np.power(self.scale_base, (i % (level + 2)) + 1)
                fractal_term = np.power(np.abs(x_norm[i]), self.fractal_exp * (level + 1))
                level_energy += scale_factor * fractal_term
            basin_energy += level_energy / self.nest_levels
        
        # Enhanced quantum interference coupling with dynamic frequency
        coupling_energy = 0.0
        for i in range(self.dim - 1):
            # Dynamic frequency based on position
            freq = self.quantum_freq * (1 + 0.5 * np.sin(x_norm[i]))
            exp_coupling = np.exp(self.chaos_factor * np.abs(x_norm[i] - x_norm[i+1]))
            sin_coupling = np.sin(freq * (x_norm[i] + x_norm[i+1]))
            coupling_energy += self.coupling_strength * exp_coupling * sin_coupling
        
        # Quantum interference patterns with nested structure
        quantum_energy = 0.0
        for i in range(self.dim):
            freq_term = self.quantum_freq * (i + 1) / (self.dim + 1)
            # Nested quantum terms
            nested_term = 0.0
            for level in range(1, self.nest_levels + 1):
                nested_term += np.sin(freq_term * x_norm[i] * level) * np.cos(freq_term * x_norm[i] * level)
            quantum_energy += self.quantum_amp * nested_term / self.nest_levels
        
        # Modified polynomial attraction basins with nested complexity
        modal_energy = 0.0
        for i in range(self.dim):
            # Nested polynomial terms
            poly_terms = []
            for level in range(1, self.nest_levels + 1):
                term = x_norm[i]**(4 * level) - (5 * level) * x_norm[i]**(3 * level) + (10 * level) * x_norm[i]**(2 * level) - (10 * level) * x_norm[i]**level + level
                poly_terms.append(term)
            combined_poly = np.sum(poly_terms) / self.nest_levels
            trig_term = np.sin(self.quantum_freq * x_norm[i] * self.nest_levels)
            modal_energy += (combined_poly + self.quantum_amp * trig_term)**2
        
        # Combined energy with dynamic scaling
        total_energy = (basin_energy + coupling_energy + quantum_energy + 
                       modal_energy) / self.dim
        
        # Add controlled noise for increased ruggedness with chaotic component
        noise = self.ruggedness * np.random.rand() * (1 + 0.6 * np.sin(np.sum(x_norm**6)))
        
        return total_energy + noise