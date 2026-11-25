import numpy as np

class HyperEllipticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.spectral_decay = 0.9
        self.harmonic_amplitude = 2.0
        self.condition_number = 500.0
        self.resolution_levels = min(7, dim)
        self.fractal_exponent = 1.7
        self.quantum_phase = np.random.rand(dim) * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spectral filtering with chaotic frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = np.sin(i * 1.3 + self.quantum_phase[i % len(self.quantum_phase)]) * 0.5 + 1.0
            freq_weight = np.exp(-self.spectral_decay * i) * freq_mod
            spectral_term += freq_weight * (x[i] ** 2) * (1.0 + 0.3 * np.sin(x[i] * 4.0 + i))
        
        # Multi-resolution harmonic coupling with quantum-like interference
        harmonic_term = 0.0
        for level in range(1, self.resolution_levels + 1):
            level_weight = 1.0 / (level ** self.fractal_exponent)
            level_sum = 0.0
            for i in range(self.dim):
                freq = 2.0 ** level + np.sin(i * 0.7) * 0.5
                phase_shift = self.quantum_phase[i % len(self.quantum_phase)]
                level_sum += (np.sin(x[i] * freq + phase_shift) * 
                             np.cos(x[i] * freq * 0.3 + phase_shift))
            harmonic_term += level_weight * (level_sum ** 2)
        
        # Condition number modulation with fractal scaling
        condition_mod = 1.0 + (self.condition_number - 1.0) * (np.sum(x**4) / (self.dim * 625.0)) ** 0.5
        
        # Cross-dimensional coupling with chaotic elliptic geometry and fractal interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.05)
                # Fractal interaction term with chaotic modulation
                fractal_mod = np.sin(dist * 3.0 + i * 0.3) * 0.2 + 1.0
                cross_term += (1.0 / (dist + 0.05)) * np.sin(x[i] * x[j]) * fractal_mod
        
        # Adaptive amplitude scaling with chaotic modulation
        amp_scale = self.harmonic_amplitude * (1.0 + 0.3 * np.log(self.dim + 1) + 
                                               np.sin(np.sum(x) * 0.5) * 0.2)
        
        return condition_mod * (0.3 * spectral_term + 0.4 * harmonic_term + 0.3 * cross_term)