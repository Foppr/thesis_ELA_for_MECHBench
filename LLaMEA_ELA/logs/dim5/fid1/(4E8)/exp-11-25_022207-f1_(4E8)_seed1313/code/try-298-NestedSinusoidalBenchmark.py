import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested = 0
        for i in range(self.dim):
            freq = 2**(i % 6)  # Frequencies 1, 2, 4, 8, 16, 32
            amp = 1.0 / (1.0 + 0.1 * i)
            nested += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Dynamic conditioning weights that change based on position
        conditioning = 0
        for i in range(self.dim):
            # Position-dependent weights
            weight = 1.0 + 0.5 * np.sin(2 * np.pi * x_norm[i])
            conditioning += weight * x_norm[i]**4
        
        # Cross-dimensional coupling with nested interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nested coupling terms with sinusoidal modulation
                coupling_term = np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
                coupling += coupling_term / (1.0 + 0.1 * (i + j))
        
        # Multi-scale oscillatory patterns with chaotic phase shifts
        oscillatory = 0
        for i in range(self.dim):
            # Phase shift dependent on previous dimensions
            phase_shift = np.sum(x_norm[:i]) if i > 0 else 0
            oscillatory += np.sin(3 * np.pi * x_norm[i] + phase_shift) * np.cos(4 * np.pi * x_norm[i] + phase_shift)
        
        # Asymmetric barrier terms with exponential scaling
        barriers = 0
        for i in range(self.dim):
            if x_norm[i] > 0:
                barriers += 2.0 * np.exp(-x_norm[i]**2) + 0.5 * x_norm[i]**6
            else:
                barriers += 1.5 * np.exp(-x_norm[i]**2) + 0.3 * x_norm[i]**8
        
        # Combined function with adaptive scaling factors
        result = 1.5 * nested + 1.0 * conditioning + 0.8 * coupling + 0.6 * oscillatory + 0.4 * barriers
        
        return result