import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave interactions with adaptive frequencies based on dimension
        chaotic_interaction = 0.0
        for i in range(self.dim):
            freq_i = 2 * (i + 1) * np.pi
            for j in range(i+1, self.dim):
                freq_j = 2 * (j + 1) * np.pi
                chaotic_interaction += np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * np.sin((freq_i + freq_j) * (x_norm[i] - x_norm[j]))
        
        # Asymmetric polynomial potentials with varying exponents
        asym_poly = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.5 * np.sin(i * np.pi / self.dim)
            asym_poly += (x_norm[i]**(4 + exp_factor) + 0.5 * x_norm[i]**(3 + exp_factor)) * np.cos(2 * np.pi * x_norm[i])
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_coupling += np.exp(-dist) * (x_norm[i]**3 + x_norm[j]**3) * np.sin(5 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Fractal-like harmonic components with recursive modulation
        fractal_harmonic = 0.0
        for i in range(self.dim):
            mod_freq = 3 * (i + 1) * np.pi
            fractal_harmonic += np.sin(mod_freq * x_norm[i]**2) * np.cos(mod_freq * x_norm[i]) * np.sin(2 * mod_freq * x_norm[i])
        
        # Add noise and scale
        noise = 0.01 * np.random.random()
        
        return 1.5 * chaotic_interaction + 0.8 * asym_poly + 0.6 * cross_coupling + 0.4 * fractal_harmonic + noise