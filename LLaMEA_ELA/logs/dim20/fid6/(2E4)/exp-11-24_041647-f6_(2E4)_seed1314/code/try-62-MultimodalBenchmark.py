import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic basin term with dimension-dependent scaling and non-linear modulation
        quadratic_term = 0.4 * np.sum(x_normalized**2) * (1 + 0.15 * self.dim + 0.05 * np.sin(0.3 * self.dim))
        
        # Chaotic sinusoidal components with exponential decay, dynamic frequencies, and amplitude modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 20 * (1.8 ** i) * (1 + 0.4 * np.sin(0.6 * i))
            amp_mod = 1.0 + 0.2 * np.cos(0.5 * i)
            chaotic_term += amp_mod * np.sin(freq * x_normalized[i]) * np.exp(-0.4 * i) * (1 + 0.4 * x_normalized[i]**3)
        
        # Cross-dimensional interactions with variable coupling strength, dynamic phase shifts, and interaction modulations
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.7 * (1 - np.exp(-0.2 * (i + j))) * (1 + 0.3 * np.cos(0.4 * (i - j)))
                phase_shift = 0.15 * np.sin(0.5 * (i + j))
                interaction_mod = 1.0 + 0.1 * np.sin(0.2 * i) * np.cos(0.3 * j)
                cross_term += coupling * interaction_mod * np.sin(12 * np.pi * x_normalized[i] + phase_shift) * np.cos(9 * np.pi * x_normalized[j] + phase_shift)
        
        # Dynamic global minimum shift with enhanced complexity and multi-scale modulation
        shift = 0.5 * (self.dim / 20.0)
        shift_term = 1.2 * np.sum((x_normalized - shift)**3) + 0.6 * np.sum((x_normalized + shift)**3)
        
        # Additional high-frequency oscillatory component with multi-scale frequency and amplitude modulation
        high_freq_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.4 * i)
            amp_mod = 1.0 + 0.25 * np.cos(0.6 * i)
            high_freq_term += amp_mod * np.sin(freq_mod * 30 * x_normalized[i]) * np.cos(freq_mod * 22 * x_normalized[i]) * np.exp(-0.25 * i)
        
        # Add a novel hybrid term combining polynomial and trigonometric components for increased multimodality
        hybrid_term = 0.0
        for i in range(self.dim):
            hybrid_term += (x_normalized[i]**5) * np.sin(15 * x_normalized[i]) * (1 + 0.2 * np.cos(3 * x_normalized[i]))
        
        return quadratic_term + chaotic_term + cross_term + shift_term + high_freq_term + hybrid_term