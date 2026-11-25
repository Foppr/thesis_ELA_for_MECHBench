import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic coupling parameters
        self.chaos_factor = 2.5
        self.coupling_strength = 1.2
        # Modified fractal scaling
        self.fractal_exp = 1.3
        self.scale_base = 1.6
        # Quantum-inspired interference
        self.quantum_amp = 0.7
        self.quantum_freq = 3.14159 * 2
        # Ruggedness control
        self.ruggedness = 0.05
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Enhanced fractal basin structure with dynamic scaling
        basin_energy = 0.0
        for i in range(self.dim):
            scale_factor = np.power(self.scale_base, (i % 7) / 2.0)
            basin_term = np.power(np.abs(x_norm[i]), self.fractal_exp) * scale_factor
            basin_energy += basin_term
        
        # Exponential sinusoidal coupling with phase modulation
        coupling_energy = 0.0
        for i in range(self.dim - 1):
            exp_coupling = np.exp(self.chaos_factor * np.abs(x_norm[i] - x_norm[i+1]))
            phase_shift = np.sin(0.5 * np.pi * (i / self.dim))
            sin_coupling = np.sin(self.quantum_freq * (x_norm[i] + x_norm[i+1]) + phase_shift)
            coupling_energy += self.coupling_strength * exp_coupling * sin_coupling
        
        # Quantum interference patterns with frequency modulation
        quantum_energy = 0.0
        for i in range(self.dim):
            freq_term = self.quantum_freq * (i + 1) / self.dim * (1 + 0.3 * np.sin(i * 0.7))
            quantum_energy += self.quantum_amp * np.sin(freq_term * x_norm[i]) * np.cos(freq_term * x_norm[i])
        
        # Modified polynomial attraction basins with cross-terms
        modal_energy = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**6 - 4 * x_norm[i]**4 + 5 * x_norm[i]**2 - 1
            trig_term = np.sin(2 * self.quantum_freq * x_norm[i])
            cross_term = 0.0
            for j in range(i):
                cross_term += np.sin(self.quantum_freq * (x_norm[i] - x_norm[j]))
            modal_energy += (poly_term + self.quantum_amp * trig_term + 0.3 * cross_term)**2
        
        # Combined energy with ruggedness
        total_energy = (basin_energy + coupling_energy + quantum_energy + 
                       modal_energy) / self.dim
        
        # Add controlled noise for increased ruggedness with spatial correlation
        noise = self.ruggedness * np.random.rand() * (1 + 0.5 * np.sin(np.sum(x_norm**3)))
        
        return total_energy + noise