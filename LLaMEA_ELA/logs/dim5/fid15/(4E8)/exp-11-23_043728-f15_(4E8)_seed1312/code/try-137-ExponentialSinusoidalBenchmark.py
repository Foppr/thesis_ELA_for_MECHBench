import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic coupling parameters
        self.chaos_factor = 2.1
        self.coupling_strength = 0.8
        # Modified fractal scaling
        self.fractal_exp = 1.1
        self.scale_base = 1.4
        # Quantum-inspired interference
        self.quantum_amp = 0.5
        self.quantum_freq = 2.5 * np.pi
        # Ruggedness control
        self.ruggedness = 0.03
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Enhanced fractal basin structure
        basin_energy = 0.0
        for i in range(self.dim):
            scale_factor = np.power(self.scale_base, i % 5)
            basin_term = np.power(np.abs(x_norm[i]), self.fractal_exp) * scale_factor
            basin_energy += basin_term
        
        # Exponential sinusoidal coupling
        coupling_energy = 0.0
        for i in range(self.dim - 1):
            exp_coupling = np.exp(self.chaos_factor * np.abs(x_norm[i] - x_norm[i+1]))
            sin_coupling = np.sin(self.quantum_freq * (x_norm[i] + x_norm[i+1]))
            coupling_energy += self.coupling_strength * exp_coupling * sin_coupling
        
        # Quantum interference patterns
        quantum_energy = 0.0
        for i in range(self.dim):
            freq_term = self.quantum_freq * (i + 1) / self.dim
            quantum_energy += self.quantum_amp * np.sin(freq_term * x_norm[i]) * np.cos(freq_term * x_norm[i])
        
        # Modified polynomial attraction basins
        modal_energy = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**6 - 4 * x_norm[i]**4 + 5 * x_norm[i]**2 - 1
            trig_term = np.sin(2 * self.quantum_freq * x_norm[i])
            modal_energy += (poly_term + self.quantum_amp * trig_term)**2
        
        # Combined energy with ruggedness
        total_energy = (basin_energy + coupling_energy + quantum_energy + 
                       modal_energy) / self.dim
        
        # Add controlled noise for increased ruggedness
        noise = self.ruggedness * np.random.rand() * (1 + 0.4 * np.sin(np.sum(x_norm**3)))
        
        return total_energy + noise